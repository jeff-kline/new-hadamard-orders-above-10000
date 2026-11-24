# Verification record

## Environment of the pinned run (2026-11-24)

- macOS, x86_64, one core, run under `nice`, BLAS limited to one thread.
- Python 3.9 with NumPy, in an isolated virtual environment; `code/golay/` uses only the
  standard library.
- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2021).

`make fetch` downloads Zaitsev's `QH566.txt` (no license is stated on its page, so it is not
redistributed) and checks SHA-256
`4fbdcd2f44c7d654c2328992a44fbeafac6783ad91862137169d1c732da64355`. Kumar's certificate
`inputs/C1286.json` (Apache-2.0) is included. Hashes of all tracked files are in
[MANIFEST.sha256](MANIFEST.sha256).

## Commands

```sh
make verify PY=/path/to/python       # about 1 minute
make verify-big PY=/path/to/python   # about 5 minutes, 2 GB
make paper
```

Each target writes to `build/` and compares byte for byte with `evidence/`, printing `MATCH`.

## What the checks cover

| Output | Checks |
|---|---|
| [evidence/orders.txt](evidence/orders.txt) | dense controls H(76), H(396); Kumar's order-1286 quaternary matrix and H(2572), dense; Lemma 1 on non-Hermitian quartic cores (q' = 5, r = 3, 5; q' = 13, r = 3), dense; orders 159052 and 824332: input core exact, Yamada pair exact, power core Gram on random vectors, coded K* is the adjoint of K, K K* = K* K = 2(q+2) I on three random vectors each, unit entries on sampled rows and columns, a corrupted core fails |
| [evidence/orders-big.txt](evidence/orders-big.txt) | the same for 22425772 (two random vectors) |
| [evidence/openness.txt](evidence/openness.txt) | the over-approximating sieve of Section 4 for the three orders, with positive controls 2572, 5788, 9172 and the open orders 2396, 9356 |
| [evidence/golay.txt](evidence/golay.txt) | exact Gram identity of the matrices of orders 160 (control), 25072, 46192, 47968 by cyclic polynomial multiplication, input pairs, a corrupted coefficient fails |

The random checks detect any single wrong entry with probability at least 1/2 per vector; they
do not replace the proofs. The large matrices are never stored.

## Paper

`make paper` builds [paper/main.pdf](paper/main.pdf) in three passes with
`SOURCE_DATE_EPOCH` fixed.

PDF SHA-256: `9e4a08fc8d53943ff9ce79e9b6cadcc5ae66d339a569e2e49b883d3307e30ce9`
