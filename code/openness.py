"""Over-approximating sieve: is order N = 4m (m odd) reached by a construction in Egan, Kotsireas,
London and O Cathain (arXiv 2610.27175) Table 4, or by a 2026 family, from inputs known before this
note?  Every ingredient set is deliberately TOO LARGE, so "not reached" is robust; "reached" may be
a false alarm and is printed with its route for inspection.

Over-approximations (each is a superset of what is published):
  T(t)   : t <= 200; t = g, 2g+1, g+g' (g Golay); 2n+1 (n <= 43 or n Golay); 3n-1 (n even <= 46);
           and every product of such numbers (Yang multiplication allowed for all factors).
  WT(w)  : every odd w < 2000; (q+1)/2 and q for prime powers q = 1 mod 4 (no products: only 2uv is known).
  H(4s)  : every s < 2500 except the open orders of EKLO Table 5 (minus 2026 closures); for larger odd s,
           every order this sieve itself reaches (recursively); every even s.
  skew / symmetric conference / quaternary conference cores: any order c <= 4000, any c with c-1 a
           prime power, Mathon and Seberry-Whiteman orders.
"""
import sys
from functools import lru_cache

def fac(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1 if p == 2 else 2
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def pp(n): return n > 1 and len(fac(n)) == 1
def divisors(n):
    ds = [1]
    for p, a in fac(n).items(): ds = [d * p ** k for d in ds for k in range(a + 1)]
    return sorted(ds)

LIM = 10 ** 8
GOLAY = sorted({2 ** a * 10 ** b * 26 ** c for a in range(30) for b in range(10) for c in range(8)
                if 2 ** a * 10 ** b * 26 ** c < LIM})
GSET = set(GOLAY)
def t_base(t):
    if t <= 200: return True
    if t in GSET or (t % 2 == 1 and (t - 1) // 2 in GSET): return True
    if t % 2 == 1 and (t - 1) in GSET: return True                 # g + g' with one of them 1
    if t % 2 == 1 and ((t - 1) // 2 <= 43): return True
    if (t + 1) % 3 == 0 and (t + 1) // 3 % 2 == 0 and (t + 1) // 3 <= 46: return True
    return False
@lru_cache(None)
def T(t):  # product closure
    if t_base(t): return True
    return any(T(d) and T(t // d) for d in divisors(t) if 1 < d < t)
def w_base(w):
    if w % 2 == 1 and w < 2000: return True
    if pp(w) and w % 4 == 1: return True
    if pp(2 * w - 1) and (2 * w - 1) % 4 == 1: return True
    return False
def WT(w): return w_base(w)   # no product closure: only 2uv is published, and it is even
# EKLO 2610.27175v2 Table 5 (orders <= 1e4 with no known matrix), minus the 2026 closures by Kumar
OPEN = set(4 * p for p in [599, 643, 719, 739, 751, 839, 859, 863, 907, 947, 971, 1019, 1031, 1039, 1051, 1087,
    1103, 1187, 1223, 1259, 1283, 1291, 1319, 1327, 1367, 1423, 1427, 1439, 1451, 1471, 1487, 1499, 1543, 1559,
    1567, 1571, 1579, 1583, 1619, 1663, 1667, 1699, 1747, 1783, 1787, 1831, 1847, 1871, 1879, 1907, 1979, 1987,
    2027, 2039, 2063, 2083, 2087, 2099, 2203, 2207, 2251, 2287, 2339, 2347, 2371, 2383, 2399, 2423, 2459]) \
    | {2676, 5028, 5748, 5892, 6852, 7572, 7716, 3820, 4460, 7180, 8380, 8860, 9260, 4676, 7924, 9716, 6876,
       7876, 8684, 9308}
OPEN -= {2572, 3356, 3436, 3820, 4204, 6796}
@lru_cache(None)
def H4(s):
    # H(4s) for odd s: known below 1e4 unless listed open; above 1e4, reached by any route of this
    # sieve (recursively), so the over-approximation is preserved.
    if s < 2500: return 4 * s not in OPEN
    if s % 2 == 0: return True          # 4s divisible by 8: not tested here, treated as known
    return bool(routes(4 * s))
def mathon_orders(lim):
    return {q * q * (q + 2) + 1 for q in range(3, 2000) if pp(q) and q % 4 == 3 and pp(q + 2) and q * q * (q + 2) + 1 < lim}
def conf_like(c):  # skew / symmetric / quaternary conference cores, over-approximated
    return c <= 4000 or pp(c - 1) or c in mathon_orders(10 ** 12) or any(5 * 9 ** (2 * t + 1) + 1 == c for t in range(10))

def routes(N):
    assert N % 4 == 0 and (N // 4) % 2 == 1
    m = N // 4; out = []
    if pp(4 * m - 1): out.append("Paley I")
    if pp(2 * m - 1) and (2 * m - 1) % 4 == 1: out.append("Paley II")
    if WT(m): out.append("Williamson array WT(m)")
    for t in divisors(m):
        if 1 < t and T(t) and WT(m // t): out.append(f"Cooper-Wallis T({t}) x WT({m // t})")
        if 1 < t and T(t) and H4(m // t): out.append(f"Seberry-Yamada product T({t}) x H(4*{m // t})")
    if pp(m) and m % 4 == 1: out.append("Miyamoto I")
    if any(1 + q + q * q == m for q in range(2, 5000) if pp(q)): out.append("Spence")
    if (N // 2) in mathon_orders(10 ** 12): out.append("Mathon")
    if any(2 * (5 * 9 ** (2 * t + 1) + 1) == N for t in range(10)): out.append("Seberry-Whiteman")
    q = m - 2
    if pp(q) and q % 4 == 1 and conf_like((q + 3) // 2):
        out.append(f"Yamada / Kumar 4(q+2), q={q}, core order {(q + 3) // 2} (over-approx)")
    if (m - 3) % 4 == 0:
        r = (m - 3) // 4; s = int(round(r ** 0.5))
        if s * s == r and pp(s): out.append("EKLO Thm 7 family 4(4q^2+3)")
    return out

if __name__ == "__main__":
    for N in map(int, sys.argv[1:]):
        m = N // 4
        rs = routes(N)
        print(f"{N} = 4*{m}, m = {fac(m)}: {'NOT REACHED' if not rs else 'REACHED by ' + '; '.join(rs)}")
