# Admission record

**Current state:** CANDIDATE

**Verdict:** NOT YET ADMITTED

**Version:** 0.1.0 (release candidate)

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** The author approved the paper's abstract and the
README introduction on 2026-11-24.

## Principal claims

1. Theorem A: a quaternary conference matrix of order $n+1$ ($n$ odd) and a
   prime $q=2n^r-1$ give a Hadamard matrix of order $4(2n^r+1)$.
2. Theorem B: Hadamard matrices of orders $159052=4\cdot17\cdot2339$,
   $824332=4\cdot206083$ and $22425772=4\cdot31\cdot223\cdot811$, not
   reached by the constructions listed in Section 4 of the paper from
   previously known ingredients.
3. Theorem C: two dihedral Golay pairs (or complex Golay pairs) of lengths
   $m,n$ give a Hadamard matrix of order $16(m+n)$.
4. Theorem D: Hadamard matrices of orders $25072=16\cdot1567$,
   $46192=16\cdot2887$ and $47968=32\cdot1499$, each half
   the smallest order recorded in Kumar's 2026 table for its odd part.

## Gates

| Gate | Status |
|---|---|
| P1 prior work | PASS with residuals: searches of 24 Nov 2026 in [audit/PRIOR-ART.md](audit/PRIOR-ART.md) and [audit/reviews/p1-rescan-2026-11-24.md](audit/reviews/p1-rescan-2026-11-24.md); not accessible: Seberry–Yamada's enumeration below 40000, Delsarte–Goethals–Seidel 1971, Craigen's unit-weighing papers, Geramita–Seberry Appendix K, Koukouvinos 1988; aiXiv has no usable search |
| A1 consistency | PASS: proof audit, claims/citation audit and an end-to-end read of the assembled paper (24 Nov 2026); all findings dispositioned in [audit/LEDGER.md](audit/LEDGER.md) |
| R1 stewardship | open: no tag, archive or DOI |
