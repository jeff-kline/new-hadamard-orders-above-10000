"""Verification of Theorems A and B (squared quaternary conference cores + Kumar's template).

Usage:  python code/verify_orders.py            # controls, 159052, 824332 (about a minute, one core)
        python code/verify_orders.py --big      # also 22425772 (about four minutes, 2 GB)

Inputs: inputs/C1286.json (Kumar, Apache-2.0) and inputs/QH566.txt (Zaitsev; fetched by `make fetch`).
Output is deterministic (seeded random vectors; booleans and integers only).
"""
import json, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import certify as C
import power as P

ROOT = os.path.join(os.path.dirname(__file__), "..")
SYM = {'1': 1, '-': -1, 'i': 1j, 'j': -1j}

def out(name, value):
    print(f"{name}: {json.dumps(value, sort_keys=True, default=str)}")

def strip(d):
    if isinstance(d, dict): return {k: strip(v) for k, v in d.items() if k != "max_round_residual"}
    return d

def zaitsev_core():
    H = np.array([[SYM[c] for c in l.strip()] for l in open(os.path.join(ROOT, "inputs/QH566.txt")) if l.strip()], dtype=complex)
    gram = bool(np.array_equal(H @ H.conj().T, 566 * np.eye(566)))
    Yp = H[1:283, 284:]
    layout = bool(np.array_equal(Yp[:141, :141] - Yp[:141, 141:], 2 * np.eye(141)))
    Z = Yp[:141, :141] - np.eye(141)
    Q = np.block([[np.zeros((1, 1)), np.ones((1, 141))], [np.ones((141, 1)), Z]])
    Zn, ok = C.normal_core(Q)
    return Zn, dict(QH566_gram=gram, template_layout=layout, QC142=C.check_qc(Q), core_normal=ok,
                    nonreal=bool(np.any(Z.imag != 0)), hermitian=bool(np.array_equal(Zn, Zn.conj().T)))

def chain(Z, r, trials):
    n0 = Z.shape[0]; nn = n0 ** r; q = 2 * nn - 1
    rep = dict(n0=n0, r=r, q=q, q_prime=C.is_prime(q), q_mod_8=q % 8, real_order=4 * (q + 2))
    mv, mvh = C.squared_core_mv(Z) if r == 2 else P.implicit_power_mv(Z, r)
    g = True
    for _ in range(trials):
        x = C.rng.choice(np.array([1, -1, 1j, -1j]), size=nn)
        g &= bool(np.array_equal(mv(mvh(x)), nn * x - x.sum())) and bool(np.array_equal(mvh(mv(x)), nn * x - x.sum()))
    rep["power_core_gram"] = g
    e1 = np.ones(nn, complex); rep["power_core_zero_sums"] = bool(np.all(mv(e1) == 0) and np.all(mvh(e1) == 0))
    al, be, yinfo = C.yamada(q); rep["yamada"] = yinfo
    T = C.Template(q, al, be, mv, mvh)
    rep["K_order"] = T.size
    ok = True
    for _ in range(2):
        x = C.rng.choice(np.array([1, -1, 1j, -1j]), size=T.size); y = C.rng.choice(np.array([1, -1, 1j, -1j]), size=T.size)
        ok &= bool(np.vdot(y, T.K(x)) == np.vdot(T.Kh(y), x))
    rep["coded_Kstar_is_adjoint_of_K"] = ok
    rep["freivalds_KKstar_and_KstarK"] = C.freivalds(T, trials)
    cols = [0, 1, T.size // 2, T.size - 1] + [int(c) for c in C.rng.integers(0, T.size, 3)]
    rep["unit_entries_checked_rows_cols"] = C.column_units(T, cols)
    Zb = Z.copy(); Zb[3, 9] *= -1
    mvb, mvhb = C.squared_core_mv(Zb) if r == 2 else P.implicit_power_mv(Zb, r)
    rep["negative_control_flipped_core_entry_fails"] = not any(C.freivalds(C.Template(q, al, be, mvb, mvhb), 1))
    return rep

if __name__ == "__main__":
    big = "--big" in sys.argv
    out("dense controls (Paley QC(4), QC(8) squared -> H(76), H(396))", strip(C.run_control()))
    kum, Zk = C.run_kumar(json.load(open(os.path.join(ROOT, "inputs/C1286.json"))))
    out("Kumar's instance q=641 -> H(2572), dense", strip(kum))
    for p in (5, 13):
        Zq = P.quartic_core(p)
        for r in ((3, 5) if p == 5 else (3,)):
            W = P.dense_power(Zq, r)
            out(f"power lemma, quartic core q'={p}, r={r}", P.core_ok(W))
    out("order 824332 = 4(2*321^2+1)", chain(Zk, 2, 3))
    Zz, zinfo = zaitsev_core()
    out("Zaitsev QH566 core", zinfo)
    out("order 159052 = 4(2*141^2+1)", chain(Zz, 2, 3))
    if big:
        out("order 22425772 = 4(2*141^3+1)", chain(Zz, 3, 2))
    out("FFT rounding residual below 1e-6", C.RES["max_round_residual"] < 1e-6)
