# New Hadamard orders above $10^4$

Jeffery Kline

[![Version DOI: 10.5281/zenodo.24517277](https://zenodo.org/badge/DOI/10.5281/zenodo.24517277.svg)](https://doi.org/10.5281/zenodo.24517277)

**Status: version 0.1.0 admitted 2026-11-24.** The immutable release is
[`v0.1.0`](https://github.com/jeff-kline/new-hadamard-orders-above-10000/releases/tag/v0.1.0), archived at version DOI
[`10.5281/zenodo.24517277`](https://doi.org/10.5281/zenodo.24517277). The concept DOI
[`10.5281/zenodo.24517276`](https://doi.org/10.5281/zenodo.24517276) resolves to the latest version; cite the
version DOI for reproducibility. Admission under the project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html)
is a release decision, not peer review or a correctness certificate; see
[ADMISSION.md](ADMISSION.md). The tagged snapshot retains its prepublication
“release candidate” wording because the DOI did not exist when it was made.

The paper is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex).

## Introduction

A Hadamard matrix is a square matrix of 1s and −1s whose rows are pairwise
orthogonal. Such matrices are conjectured to exist in every size divisible by 4.
We construct them in six sizes: $159052=4\cdot17\cdot2339$,
$824332=4\cdot206083$, $22425772=4\cdot31\cdot223\cdot811$,
$25072=16\cdot1567$, $46192=16\cdot2887$ and $47968=32\cdot1499$.

The first three come from one theorem. Suppose a quaternary conference matrix
of size $n+1$ exists: a matrix with zero diagonal, entries $\pm1$ and
$\pm i$ elsewhere, and orthogonal rows. If $n$ is odd and $q=2n^r-1$ is
prime for some $r\ge1$, then a Hadamard matrix of size $4(2n^r+1)$ exists.
The proof raises the conference matrix to size $n^r+1$ by Turyn's power
construction, which we extend to quaternary matrices without symmetry, and
feeds it to Kumar's 2026 quaternary form of Yamada's construction of size
$4(q+2)$. The inputs are quaternary conference matrices of sizes 142 and 322,
published by Zaitsev and by Kumar. No printed table of known Hadamard sizes
covers these three sizes, so here "new" means that none of the constructions
listed in Section 4 of the paper reaches them from previously known
ingredients. The odd part 206083 of the second size is a prime congruent to
3 modulo 4, so product constructions do not apply to it.

The last three come from a second construction, which gives a Hadamard matrix
of size $16(m+n)$ from two dihedral Golay pairs of lengths $m$ and $n$. These
are pairs of sequences over the symbols $\pm1$, $\pm i$, $\pm s$, introduced
by Kamali and Kharaghani, with $i^2=-1$, $s^2=1$ and $is=-si$. Placing the two
pairs on separate tensor factors makes them commute. Each of the three sizes is
half the smallest size previously recorded for its odd part in Kumar's 2026
table.

## What is new

Turyn's power construction for conference matrices (extended by Glazyrin to
Hermitian unit-modulus matrices) and Kumar's 2026 quaternary form of Yamada's
construction were known; Kumar used the latter to settle five open sizes below
$10^4$. The six sizes, and the construction that gives each:

| Size | Factorization | Construction |
|---:|---|---|
| 159052 | $4\cdot17\cdot2339$ | Theorem A, $n=141$, $r=2$ |
| 824332 | $4\cdot206083$ | Theorem A, $n=321$, $r=2$ |
| 22425772 | $4\cdot31\cdot223\cdot811$ | Theorem A, $n=141$, $r=3$ |
| 25072 | $16\cdot1567$ | Theorem C, lengths $7+1560$ |
| 46192 | $16\cdot2887$ | Theorem C, lengths $7+2880$ |
| 47968 | $32\cdot1499$ | Theorem C, lengths $182+2816$ |

The odd parts 206083, 1567, 2887 and 1499 are prime.

- **Principal result.** Hadamard matrices of sizes $159052=4\cdot17\cdot2339$,
  $824332=4\cdot206083$ and $22425772=4\cdot31\cdot223\cdot811$ (Theorem B). None of these sizes is reached by the constructions in Table 4
  of the 2026 survey of Egan, Kotsireas, London and Ó Catháin, or by the 2026
  families we checked, from previously known ingredients.
- **Theorem A.** If a quaternary conference matrix of size $n+1$ exists with
  $n$ odd, and $q=2n^r-1$ is prime for some $r\ge1$, then a Hadamard matrix of
  size $4(2n^r+1)$ exists.
- Turyn's power construction holds for quaternary conference matrices with no
  symmetry (Lemma 1). The proof is Turyn's and Glazyrin's with one
  substitution, so this is a small extension, not a new method.
- A table of further exponents $r$ for the other published quaternary
  conference matrices (Section 5). Those orders are not certified or tested
  for newness.
- **Theorem C.** Two dihedral Golay pairs (or complex Golay pairs) of lengths
  $m$ and $n$ give a Hadamard matrix of size $16(m+n)$. The array is Craigen's
  form of the Goethals–Seidel array, as used by Kamali and Kharaghani; the new step is to represent the two pairs on independent
  tensor factors so that they commute. For two complex pairs, Craigen, Holzmann
  and Kharaghani already give $8(m+n)$; the new cases have a dihedral pair.
- **Theorem D.** Hadamard matrices of sizes $25072=16\cdot1567$,
  $46192=16\cdot2887$ and $47968=32\cdot1499$. Kumar's table records only
  twice these sizes for the three odd parts. The sizes $4\cdot1567$,
  $4\cdot2887$ and $4\cdot1499$ remain open; these results lower the least
  known power of 2 for the three odd parts.
- Theorem C, and a classical larger-fill variant of order $16k(m+n)$, give
  further sizes up to $10^6$ (85 and 29 respectively) for which no earlier
  construction was located. We do not claim them: no table covers them, and
  our comparison there is incomplete.

Not new: the power construction (Turyn; Belevitch for $r=2$; Glazyrin for the
Hermitian case), Kumar's template and its two input matrices, Turyn's
doubling, Craigen's array, the Kamali–Kharaghani seeds, and Kharaghani's 1992 order
formula $4k(m+n)$, whose hypotheses these inputs do not meet. The size 47920
follows from published results of Du and Jiang; the paper notes it as a
remark. Novelty is bounded by the searches recorded in
[audit/](audit/).

## Earlier work

- **Conference matrices and their powers.** Belevitch squared a real conference
  matrix; Goethals and Seidel (1967) recorded it, and Turyn (1971) gave the
  construction for every power $n^r+1$. Glazyrin (arXiv:2608.16116, 2026,
  Lemma 4.1 and Theorem 5) showed that Turyn's construction works for
  Hermitian matrices with unit-modulus entries.
- **Order $4(q+2)$.** Yamada (1989) built Hadamard matrices of order
  $4(q+2)$ from a symmetric conference matrix or a skew Hadamard matrix of
  order $(q+3)/2$. Kumar (2026, github.com/vatskishan03/Hadamard) gave the
  quaternary form used here, which needs a quaternary conference matrix of
  that order with no symmetry, found the input matrices by computer search,
  and settled the open orders 2572, 3436, 3820, 4204 and 6796.
- **Input matrices.** The quaternary conference matrix of order 322 is
  Kumar's (certificate `C1286.json`, about 15 CPU-hours of structured
  search). The one of order 142 is the core of Zaitsev's quaternary
  Hadamard matrix of order 566, found by a method he describes as
  unpublished.
- **Golay pairs.** Kamali and Kharaghani (1998) introduced dihedral Golay
  pairs, found them at lengths 7, 9, 15 and 19 (the first three are used here), and combined one with a binary
  pair. Kharaghani (1992) gave the order formula $4k(m+n)$ for block Golay
  inputs under an amicability hypothesis that the inputs here do not meet.
  Craigen, Holzmann and Kharaghani (2002) gave $8(x+y)$ for complex Golay
  pairs, and Du and Jiang (arXiv:2401.15381) certified many complex Golay
  lengths.
- **Tables.** Egan, Kotsireas, London and Ó Catháin (arXiv:2610.27175, 2026)
  list the open orders up to $10^4$; Cati and Pasechnik (arXiv:2411.18897)
  and Kumar's table record the least known power of 2 for each odd part up to
  2999.

## Evidence and limits

| Claim | Status |
|---|---|
| Lemma 1 (power construction, no symmetry) | proved on paper ($r=2$ in full; odd $r$ by Glazyrin's argument with $W^2$ replaced by $WW^*$); checked exactly on small non-Hermitian cores |
| Kumar's template (Lemma 2) | conditional on Kumar's proof; rebuilt and checked exactly at sizes 38, 198, 1286 |
| Input matrices of sizes 142 and 322 | certified computation (exact Gram checks of the published files) |
| Sizes 159052, 824332, 22425772 | certified computation: exact ingredient checks and randomized Gram checks |
| Newness of the three sizes | computation only, against the constructions listed in Section 4, with deliberately generous inputs |
| Section 5 table | computation only; inputs other than sizes 142 and 322 not checked |
| Theorem C | proved on paper |
| Sizes 25072, 46192, 47968 | certified computation: exact Gram check of each matrix by cyclic polynomial multiplication |
| Newness of those three sizes | comparison with Kumar's table and with earlier constructions in the sources searched |

## Reproduce

Requires Python 3 with NumPy, `curl` and `shasum`. Use an isolated
interpreter, for example `make verify PY=.venv/bin/python`.

| Command | What it checks | Cost |
|---|---|---|
| `make fetch` | downloads Zaitsev's QH566 and checks its SHA-256 | one download |
| `make verify` | controls, orders 159052 and 824332, the openness sieve, and the exact Gram checks of orders 25072, 46192, 47968 | about 1 minute, one core |
| `make verify-big` | order 22425772 | about 5 minutes, 2 GB, one core |
| `make paper` | rebuilds `paper/main.pdf` | seconds |

Each target compares its output with the pinned copy in `evidence/` and
prints `MATCH`.

## Role of AI

AI assisted the derivations, the computer verification, the literature search
and the exposition under the author's direction. Process-separated AI reviews
checked the proofs and certificates; they are not independent expert peer
review, and no independent human expert has examined the proofs. The release
repository records the sources, the reviews and their dispositions.

## License

GPL-3.0-only; see [LICENSE](LICENSE). The certificate
[inputs/C1286.json](inputs/C1286.json) is Kumar's, distributed under the
Apache License 2.0 of its source repository.
