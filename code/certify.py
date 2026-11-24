"""Certify H(4(q+2)) built by: quaternary conference core QC(n0+1) --(Theorem A squaring)-->
QC(n0^2+1) --(Kumar CONFERENCE.md Theorem 3 at q = 2 n0^2 - 1)--> quaternary Hadamard K of order
2(q+2) --(Turyn)--> H(4(q+2)).

Written from the theorem statements (no third-party code). Gaussian integers are held in complex128
with integer values; every FFT result is rounded and the rounding residual is recorded.

Usage: python certify.py control      (small dense cross-checks)
       python certify.py kumar1286     (Kumar's own order-1286 instance, dense exact Gram)
       python certify.py big <cert.json>  (squared core, q = 2*321^2 - 1, implicit Freivalds checks)
"""
import json, sys, hashlib
import numpy as np

rng = np.random.default_rng(20261124)
RES = {"max_round_residual": 0.0}

def rnd(z):
    r = np.round(z.real) + 1j * np.round(z.imag)
    RES["max_round_residual"] = max(RES["max_round_residual"], float(np.max(np.abs(z - r))) if z.size else 0.0)
    return r

# ---------- arithmetic ----------
def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def is_prime(n): return n > 1 and factor(n) == {n: 1}

def gf2_mul(x, y, r, q):
    a, b = x; c, d = y
    return ((a * c + b * d * r) % q, (a * d + b * c) % q)

def gf2_pow(x, e, r, q):
    out, base = (1, 0), x
    while e:
        if e & 1: out = gf2_mul(out, base, r, q)
        base = gf2_mul(base, base, r, q); e >>= 1
    return out

def find_field(q):
    r = next(t for t in range(2, q) if pow(t, (q - 1) // 2, q) == q - 1)
    order = q * q - 1
    primes = list(factor(q - 1)) + [p for p in factor(q + 1) if p not in factor(q - 1)]
    for a in range(0, q):
        for b in range(1, 4):
            x = (a, b)
            if all(gf2_pow(x, order // p, r, q) != (1, 0) for p in primes):
                return r, x
    raise RuntimeError("no primitive element found")

def yamada(q, r=None, xi=None):
    """First rows beta (M, zero diagonal) and alpha (N) of order n = (q+1)/2."""
    assert is_prime(q) and q % 4 == 1
    n = (q + 1) // 2
    if r is None: r, xi = find_field(q)
    xi = tuple(xi)
    psi = lambda t: 0 if t % q == 0 else (1 if pow(t, (q - 1) // 2, q) == 1 else -1)
    step = gf2_pow(xi, 4, r, q)
    pa, pb = (1, 0), gf2_pow(xi, n, r, q)
    alpha = np.empty(n, dtype=np.int64); beta = np.empty(n, dtype=np.int64)
    for m in range(n):
        alpha[m] = psi(2 * pa[0]); beta[m] = psi(2 * pb[0])
        pa = gf2_mul(pa, step, r, q); pb = gf2_mul(pb, step, r, q)
    # checks: symmetry, entry pattern, PAF_alpha + PAF_beta = q*delta
    idx = (-np.arange(n)) % n
    sym = bool(np.array_equal(alpha, alpha[idx]) and np.array_equal(beta, beta[idx]))
    pattern = bool(beta[0] == 0 and np.all(np.abs(beta[1:]) == 1) and np.all(np.abs(alpha) == 1))
    fa, fb = np.fft.fft(alpha), np.fft.fft(beta)
    paf = rnd(np.fft.ifft(np.abs(fa) ** 2 + np.abs(fb) ** 2)).real
    target = np.zeros(n); target[0] = q
    paf_ok = bool(np.array_equal(paf, target))
    # exact spot checks of the PAF at random lags (pure integer arithmetic)
    lags = [0, 1, n - 1] + list(rng.integers(1, n, 40))
    exact_ok = all(int(np.dot(alpha, np.roll(alpha, -s)) + np.dot(beta, np.roll(beta, -s))) == (q if s == 0 else 0) for s in lags)
    return alpha, beta, dict(q=q, n=n, r=r, xi=list(xi), symmetric=sym, pattern=pattern,
                             paf_fft_exact=paf_ok, paf_spot_exact=exact_ok)

# ---------- quaternary conference matrices ----------
def unit(x, y):  # omega*x + conj(omega)*y for x, y in {0, +-1}
    return ((x + y) + 1j * (x - y)) / 2

def szollosi_core(cert):
    """Kumar CONFERENCE.md Theorem 1 over a cyclic group Z_m, R[g,h] = [g+h = c0]."""
    c = cert["core"]; m = int(c["group"]); c0 = int(c.get("reflection", 0))
    assert "border" not in c
    conv = {"+": 1, "-": -1, "0": 0}
    A, B, C, D = (np.array([conv[ch] for ch in s], dtype=np.int64) for s in c["sequences"])
    g = np.arange(m)
    Xf = lambda f: f[(g[None, :] - g[:, None]) % m]          # X_f[g,h] = f(h-g)
    R = ((g[:, None] + g[None, :]) % m == c0).astype(np.int64)
    X = unit(Xf(A), Xf(B))
    Y = (1 + 1j) / 2 * Xf(C) + (1 - 1j) / 2 * (Xf(D) @ R)
    Q = np.block([[X, Y], [Y.conj().T, -X.conj().T]])
    return Q

def check_qc(Q):
    c = Q.shape[0]
    offd = ~np.eye(c, dtype=bool)
    units = bool(np.all(np.diag(Q) == 0) and np.all((np.abs(Q.real) + np.abs(Q.imag))[offd] == 1)
                 and np.all((Q.real * Q.imag)[offd] == 0))
    G = Q @ Q.conj().T
    return units and bool(np.array_equal(G, (c - 1) * np.eye(c)))

def normal_core(Q):
    """Scale rows/columns by units so that row 0 and column 0 are (0,1,...,1); return Z."""
    c = Q.shape[0]
    D2 = np.ones(c, complex); D2[1:] = Q[0, 1:].conj()
    Q1 = Q * D2[None, :]
    D1 = np.ones(c, complex); D1[1:] = Q1[1:, 0].conj()
    Q2 = D1[:, None] * Q1
    assert np.all(Q2[0, 1:] == 1) and np.all(Q2[1:, 0] == 1) and Q2[0, 0] == 0
    Z = Q2[1:, 1:]
    n = c - 1
    ok = bool(np.array_equal(Z @ Z.conj().T, n * np.eye(n) - np.ones((n, n)))
              and np.all(Z.sum(0) == 0) and np.all(Z.sum(1) == 0))
    return Z, ok

def square_core_dense(Z):
    n = Z.shape[0]; I = np.eye(n); J = np.ones((n, n))
    return np.kron(Z, Z) + np.kron(I, J) - np.kron(J, I)

def paley_qc(p):
    """Real conference matrix of order p+1 (p prime) in normal form: Q = [[0, e],[chi(-1) e^T, S]]."""
    chi = lambda t: 0 if t % p == 0 else (1 if pow(t, (p - 1) // 2, p) == 1 else -1)
    S = np.array([[chi(j - i) for j in range(p)] for i in range(p)], dtype=complex)
    e = np.ones(p)
    return np.block([[np.zeros((1, 1)), e[None, :]], [chi(-1) * e[:, None], S]]).astype(complex)

# ---------- implicit template ----------
class Template:
    """K = [[X, Y],[Y*, -X*]] of Kumar's Theorem 3, with core given by a matvec for Z (order n)."""
    def __init__(self, q, alpha, beta, zmv, zhmv):
        self.q, self.n = q, (q + 1) // 2
        assert len(alpha) == self.n
        self.fa, self.fb = np.fft.fft(alpha), np.fft.fft(beta)
        self.zmv, self.zhmv = zmv, zhmv
        self.size = 2 * (2 * self.n + 1)
    def M(self, x): return rnd(np.fft.ifft(self.fb * np.fft.fft(x)))   # symmetric circulant, first row beta
    def N(self, x): return rnd(np.fft.ifft(self.fa * np.fft.fft(x)))
    def A(self, U):
        u0, u1 = U[:self.n], U[self.n:]; d = self.M(u0 - u1); s = u0 + u1
        return np.concatenate([d + s, -d + s])
    def B(self, U):
        u0, u1 = U[:self.n], U[self.n:]; d = self.N(u0 - u1)
        return np.concatenate([d, -d])
    def Xp(self, U, adj=False):
        a, b = self.A(U), self.B(U)
        w = (1 + 1j) / 2
        return rnd((np.conj(w) if adj else w) * a + (w if adj else np.conj(w)) * b)
    def Yp(self, U, adj=False):
        u0, u1 = U[:self.n], U[self.n:]
        z = (self.zhmv if adj else self.zmv)(u0 + u1)
        return np.concatenate([z + (u0 - u1), z - (u0 - u1)])
    def _X(self, u, adj):
        u0, U = u[0], u[1:]
        sgn = -1 if adj else 1
        head = u0 + sgn * U.sum()
        return np.concatenate([[head], -sgn * u0 * np.ones(2 * self.n) + self.Xp(U, adj)])
    def _Y(self, u, adj):
        u0, U = u[0], u[1:]
        head = u0 + 1j * U.sum()
        return np.concatenate([[head], -1j * u0 * np.ones(2 * self.n) + self.Yp(U, adj)])
    def K(self, x):
        h = self.size // 2; u, v = x[:h], x[h:]
        return np.concatenate([self._X(u, False) + self._Y(v, False), self._Y(u, True) - self._X(v, True)])
    def Kh(self, x):
        h = self.size // 2; u, v = x[:h], x[h:]
        return np.concatenate([self._X(u, True) + self._Y(v, False), self._Y(u, True) - self._X(v, False)])

def freivalds(T, trials=3):
    c = T.size  # K K* = c I where c = 2v = size
    out = []
    for _ in range(trials):
        x = rng.choice(np.array([1, -1, 1j, -1j]), size=T.size)
        out.append(bool(np.array_equal(T.K(T.Kh(x)), c * x)) and bool(np.array_equal(T.Kh(T.K(x)), c * x)))
    return out

def column_units(T, cols):
    ok = True
    for j in cols:
        e = np.zeros(T.size, complex); e[j] = 1
        for col in (T.K(e), T.Kh(e)):   # column j of K, and conj of row j of K
            ok &= bool(np.all((np.abs(col.real) + np.abs(col.imag)) == 1) and np.all(col.real * col.imag == 0))
    return ok

def dense_from(T):
    E = np.eye(T.size, dtype=complex)
    return np.column_stack([T.K(E[:, j]) for j in range(T.size)])

def dense_template_check(T):
    Kd = dense_from(T)
    units = bool(np.all((np.abs(Kd.real) + np.abs(Kd.imag)) == 1) and np.all(Kd.real * Kd.imag == 0))
    gram = bool(np.array_equal(Kd @ Kd.conj().T, T.size * np.eye(T.size)))
    adj = bool(all(np.array_equal(T.Kh(np.eye(T.size, dtype=complex)[:, j]), Kd.conj().T[:, j]) for j in range(T.size)))
    Kr, Ki = Kd.real.astype(np.int64), Kd.imag.astype(np.int64)
    H = np.block([[Kr + Ki, Kr - Ki], [-(Kr - Ki), Kr + Ki]])
    Hf = H.astype(np.float64); real_ok = bool(np.all(np.abs(H) == 1) and np.array_equal(Hf @ Hf.T, 2 * T.size * np.eye(2 * T.size)))
    return dict(units=units, gram=gram, adjoint_matches=adj, turyn_real_H=real_ok, real_order=2 * T.size)

def dense_core_mv(Z):
    return (lambda x: rnd(Z @ x)), (lambda x: rnd(Z.conj().T @ x))

def squared_core_mv(Z):
    n0 = Z.shape[0]; Zh = Z.conj().T
    def mv(x, ZZ):
        Xm = x.reshape(n0, n0)
        return rnd((ZZ @ Xm @ ZZ.T + Xm.sum(1, keepdims=True) - Xm.sum(0, keepdims=True)).reshape(-1))
    return (lambda x: mv(x, Z)), (lambda x: mv(x, Zh))

# ---------- runs ----------
def run_control():
    rep = {}
    # (i) Paley QC(8) (p=7) squared -> QC(50), q = 97 -> order 396; implicit vs dense
    for p in (3, 7):
        Q = paley_qc(p); assert check_qc(Q)
        Z, ok = normal_core(Q); n0 = Z.shape[0]; q = 2 * n0 * n0 - 1
        W = square_core_dense(Z)
        Wq = np.block([[np.zeros((1, 1)), np.ones((1, n0 * n0))], [np.ones((n0 * n0, 1)), W]])
        al, be, yinfo = yamada(q)
        mv, mvh = squared_core_mv(Z)
        T = Template(q, al, be, mv, mvh)
        x = rng.choice(np.array([1, -1, 1j, -1j]), size=n0 * n0)
        rep[f"p={p}"] = dict(core_ok=ok, squared_is_QC=check_qc(Wq), squared_mv_matches_dense=bool(np.array_equal(mv(x), W @ x)),
                             yamada=yinfo, dense=dense_template_check(T), freivalds=freivalds(T), real_order=4 * (q + 2))
    return rep

def run_kumar(cert):
    Q = szollosi_core(cert)
    rep = dict(qc322=check_qc(Q))
    Z, ok = normal_core(Q); rep["core_normal"] = ok
    q = cert["q"]
    al, be, yinfo = yamada(q, cert["r"], cert["xi"])
    rep["yamada"] = yinfo
    mv, mvh = dense_core_mv(Z)
    T = Template(q, al, be, mv, mvh)
    rep["dense"] = dense_template_check(T)
    return rep, Z

def run_big(cert):
    rep, Z = run_kumar(cert)
    n0 = Z.shape[0]; q = 2 * n0 * n0 - 1
    rep["n0"], rep["q"], rep["q_prime"], rep["q_mod_8"] = n0, q, is_prime(q), q % 8
    al, be, yinfo = yamada(q)
    rep["yamada_big"] = yinfo
    mv, mvh = squared_core_mv(Z)
    # squared core: zero row sums and W W* = n^2 I - J on random vectors
    nn = n0 * n0; ok = True
    for _ in range(3):
        x = rng.choice(np.array([1, -1, 1j, -1j]), size=nn)
        ok &= bool(np.array_equal(mv(mvh(x)), nn * x - x.sum()))
    rep["squared_core_gram_freivalds"] = ok
    rep["squared_core_rowsums_zero"] = bool(np.all(mv(np.ones(nn, complex)) == 0) and np.all(mvh(np.ones(nn, complex)) == 0))
    T = Template(q, al, be, mv, mvh)
    rep["K_order"], rep["real_order"] = T.size, 2 * T.size
    rep["freivalds_KKh"] = freivalds(T, 3)
    cols = [0, 1, 2, T.size // 2 - 1, T.size // 2, T.size // 2 + 1, T.size - 1] + list(rng.integers(0, T.size, 5))
    rep["units_in_checked_rows_cols"] = column_units(T, [int(c) for c in cols])
    return rep

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "control": out = run_control()
    elif mode == "kumar1286":
        cert = json.load(open(sys.argv[2])); out, _ = run_kumar(cert)
    elif mode == "big":
        cert = json.load(open(sys.argv[2])); out = run_big(cert)
    out["max_round_residual"] = RES["max_round_residual"]
    print(json.dumps(out, indent=1, default=str))
