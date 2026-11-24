"""Turyn's odd power construction (Glazyrin arXiv 2608.16116 Thm 5 for Hermitian cores) tested on
NON-Hermitian quaternary cores, then fed to Kumar's template.

W_r = sum over cyclic strings S in {W, I, J}^r (every I followed by J, every J preceded by I,
cyclically) of S_1 ⊗ ... ⊗ S_r.  Claim: if ZZ* = nI - J and ZJ = JZ = 0 then W_r W_r* = n^r I - J.

Usage: python power.py dense            (quartic-character cores, q' = 5, 13; r = 3, 5 dense exact)
       python power.py big <QH566.txt> r  (core n = 141 from Zaitsev QH566; r odd; implicit + template)
"""
import sys, json, itertools
import numpy as np
import certify as C

def strings(r):
    out = []
    for s in itertools.product("WIJ", repeat=r):
        if all((s[k] != "I" or s[(k + 1) % r] == "J") and (s[k] != "J" or s[(k - 1) % r] == "I") for k in range(r)):
            out.append("".join(s))
    return out

def dense_power(Z, r):
    n = Z.shape[0]; mats = {"W": Z, "I": np.eye(n), "J": np.ones((n, n))}
    tot = 0
    for s in strings(r):
        G = np.ones((1, 1))
        for ch in s: G = np.kron(G, mats[ch])
        tot = tot + G
    return tot

def core_ok(W):
    m = W.shape[0]; off = ~np.eye(m, dtype=bool)
    units = bool(np.all(np.diag(W) == 0) and np.all((np.abs(W.real) + np.abs(W.imag))[off] == 1) and np.all((W.real * W.imag)[off] == 0))
    gram = bool(np.array_equal(W @ W.conj().T, m * np.eye(m) - np.ones((m, m))))
    sums = bool(np.all(W.sum(0) == 0) and np.all(W.sum(1) == 0))
    return dict(units=units, gram=gram, zero_sums=sums, hermitian=bool(np.array_equal(W, W.conj().T)))

def quartic_core(p):
    g = next(x for x in range(2, p) if all(pow(x, (p - 1) // f, p) != 1 for f in C.factor(p - 1)))
    ind = {pow(g, k, p): k for k in range(p - 1)}
    chi = lambda t: 0 if t % p == 0 else 1j ** (ind[t % p] % 4)
    return np.array([[chi(y - x) for y in range(p)] for x in range(p)], dtype=complex)

def implicit_power_mv(Z, r):
    n = Z.shape[0]; Zh = Z.conj().T; S = strings(r)
    def apply(X, k, M):
        if isinstance(M, str) and M == "I": return X
        if isinstance(M, str) and M == "J": return np.broadcast_to(X.sum(axis=k, keepdims=True), X.shape)
        return np.moveaxis(np.tensordot(M, X, axes=([1], [k])), 0, k)
    def mv(x, adj):
        X = x.reshape((n,) * r); tot = np.zeros_like(X)
        for s in S:
            Y = X
            for k, ch in enumerate(s):
                Y = apply(Y, k, (Zh if adj else Z) if ch == "W" else ch)
            tot = tot + Y
        return C.rnd(tot.reshape(-1))
    return (lambda x: mv(x, False)), (lambda x: mv(x, True))

if __name__ == "__main__":
    out = {}
    if sys.argv[1] == "dense":
        for p in (5, 13):
            Z = quartic_core(p)
            Q = np.block([[np.zeros((1, 1)), np.ones((1, p))], [np.ones((p, 1)), Z]])
            out[f"q'={p} base"] = dict(qc=C.check_qc(Q), **core_ok(Z))
            for r in ((3, 5) if p == 5 else (3,)):
                W = dense_power(Z, r)
                out[f"q'={p} r={r}"] = dict(strings=strings(r) if r == 3 else len(strings(r)), **core_ok(W))
                # cross-check implicit matvec against dense
                mv, mvh = implicit_power_mv(Z, r)
                x = C.rng.choice(np.array([1, -1, 1j, -1j]), size=W.shape[0])
                out[f"q'={p} r={r}"]["implicit_matches_dense"] = bool(np.array_equal(mv(x), W @ x) and np.array_equal(mvh(x), W.conj().T @ x))
    else:
        sym = {'1': 1, '-': -1, 'i': 1j, 'j': -1j}
        H = np.array([[sym[c] for c in l.strip()] for l in open(sys.argv[2]) if l.strip()], dtype=complex)
        Z = H[1:283, 284:][:141, :141] - np.eye(141)
        Q = np.block([[np.zeros((1, 1)), np.ones((1, 141))], [np.ones((141, 1)), Z]])
        Z, ok = C.normal_core(Q)
        r = int(sys.argv[3]); n0 = Z.shape[0]; nn = n0 ** r; q = 2 * nn - 1
        out.update(core_ok=ok, n0=n0, r=r, q=q, q_prime=C.is_prime(q), q_mod_8=q % 8, real_order=4 * (q + 2))
        mv, mvh = implicit_power_mv(Z, r)
        g = True
        for _ in range(2):
            x = C.rng.choice(np.array([1, -1, 1j, -1j]), size=nn)
            g &= bool(np.array_equal(mv(mvh(x)), nn * x - x.sum())) and bool(np.array_equal(mvh(mv(x)), nn * x - x.sum()))
        out["power_core_gram_freivalds"] = g
        e1 = np.ones(nn, complex)
        out["power_core_zero_sums"] = bool(np.all(mv(e1) == 0) and np.all(mvh(e1) == 0))
        ok_u = True
        for j in [0, 1, nn - 1] + [int(t) for t in C.rng.integers(0, nn, 4)]:
            e = np.zeros(nn, complex); e[j] = 1; col = mv(e)
            mask = np.ones(nn, bool); mask[j] = False
            ok_u &= bool(col[j] == 0 and np.all((np.abs(col.real) + np.abs(col.imag))[mask] == 1) and np.all((col.real * col.imag)[mask] == 0))
        out["power_core_units_checked_cols"] = ok_u
        al, be, yinfo = C.yamada(q); out["yamada"] = yinfo
        T = C.Template(q, al, be, mv, mvh)
        out["K_order"] = T.size
        out["freivalds_KKh"] = C.freivalds(T, 2)
        cols = [0, 1, T.size // 2, T.size - 1] + [int(c) for c in C.rng.integers(0, T.size, 3)]
        out["units_in_checked_rows_cols"] = C.column_units(T, cols)
        out["max_round_residual"] = C.RES["max_round_residual"]
    print(json.dumps(out, default=str))
