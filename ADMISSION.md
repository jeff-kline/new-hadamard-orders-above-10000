# Admission record

**Current state:** ADMITTED

**Current verdict: ADMITTED** on 2026-11-24, with the qualifications and residual risks below

**Version:** 0.1.0 · tag `v0.1.0` at commit `534f6d578209e250a86e18b5092c7b7556d620d5` · version DOI [10.5281/zenodo.24517277](https://doi.org/10.5281/zenodo.24517277) · concept DOI [10.5281/zenodo.24517276](https://doi.org/10.5281/zenodo.24517276)

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
| R1 stewardship | PASS: tag `v0.1.0` (tag object 97ec5dab) at `534f6d5`; GitHub zipball pinned twice (472830 bytes, sha256 55e559cd…); Zenodo record 24517277 byte-identical to it; DOI resolves; record metadata (title, creator, version, date, GPL-3.0, software, repository) match; `make verify` and the paper build reproduced from a fresh extraction of the archive (PDF sha256 9e4a08fc…, manifest 61/61) |

## Residual risks

- Novelty is bounded to the sources searched (see [audit/PRIOR-ART.md](audit/PRIOR-ART.md)). Not accessible:
  Seberry–Yamada's enumeration of odd parts below 40000, Delsarte–Goethals–Seidel 1971, Craigen's
  unit-weighing papers, Geramita–Seberry 1979 Appendix K, Koukouvinos 1988; aiXiv has no usable search.
- For 159052, 824332 and 22425772, "new" means not reached by the constructions listed in Section 4
  of the paper; no printed table covers these orders.
- The two input cores were found by others (Kumar by computer search; Zaitsev by unpublished
  methods). Zaitsev's matrix is downloaded at verify time, not redistributed.
- The large matrices are verified by exact ingredient checks plus randomized Gram checks, not by
  forming them.
- All reviews were process-separated AI reviews, not expert peer review.

## Admission event

Admitted 2026-11-24 by the author's release decision. Site entry live at
https://jeff-kline.github.io/ (commit 07d0962). Archive verification and pins: Zenodo record
24517277; see [CORRECTIONS.md](CORRECTIONS.md) for the prepublication wording in the tag.
