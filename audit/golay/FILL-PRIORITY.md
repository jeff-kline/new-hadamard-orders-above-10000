# Historical priority for the 38 larger-fill orders

Nine orders were constructible from previously published theorems. The other 29, including **125,360**, have proved existence from the larger fill and unresolved historical priority. No source checked establishes that any one of these 29 was open immediately before this construction. The comparison checks actual theorem inputs, including for orders beyond the published tables. It uses no matrix generation. [Verdict and parameters for every order](fill-priority-38.tsv) · [Bounded arithmetic replay](fill-historical-rules.mjs)

## Order 125,360

The smallest earlier construction we verified for odd part 7,835 gives **250,720 = 8(3,840 + 27,500)** via two complex Golay lengths. The handbook OCR at 7,835 reads 7, an upper bound at exponent 7. The older explicit construction supplies exponent 5. The proposed order has exponent 4. Neither the historical table nor the modern surveys establish its status at exponent 4. At another possible input, order 6,268, EKLO explicitly records an open case. That entry is about the input. At order 12,536, an earlier ordinary Hadamard matrix would suffice by Agaian with H(20). An independent check of the 1996 ternary formulas at 125,360 also led back to H(6,268). [Historical sources and precise table coordinates](fill-historical-audit.md) · [Ternary formulas and inputs](fill-signed-audit.md) · [EKLO, November 2026 revision](https://arxiv.org/abs/2610.27175)

## Three orders by 1990

Seberry and Yamada, Corollary 29(ii), obtain symmetric Williamson-type matrices of prime order q congruent to 1 modulo 4 from a symmetric Hadamard matrix of order (q−1)/2. Corollary 40 gives H(8(2q+1)). Doubling gives the listed target. The use of symmetric inputs satisfies the amicability conditions on the identity blocks in the published proof. [Seberry and Yamada, pp. 119–120 and 130–131](https://combinatorialpress.com/article/jcmcc/Volume%2007/vol-007-paper%206.pdf) · [Authors' later treatment, Corollaries 8.8 and 8.15](https://documents.uow.edu.au/~jennie/WEBPDF/175_1992.pdf)

| Target | Prime q | Symmetric input | Earlier order before doubling |
|---:|---:|---|---:|
| 540,464 | 16,889 | H(8,444), Paley at 8,443 | 270,232 |
| 727,088 | 22,721 | H(11,360) = H(2) ⊗ H(20) ⊗ H(284), Paley at 19 and 283 | 363,544 |
| 899,120 | 28,097 | H(14,048) = H(4) ⊗ H(3,512), Paley at 3,511 | 449,560 |

For each Paley prime p here, negate the field column indices in the Paley matrix. Its core then depends on the sum of the two indices, with a symmetric correction at sum zero. The two borders can be made equal by a sign change on the border row or column. This supplies the symmetric inputs, and tensor products preserve symmetry. The arithmetic checker verifies each size and prime by trial division.

## Six orders by 2015

For the three primes Q in the table, the second Paley series gives a binary negaperiodic Golay pair of length (Q+1)/2 = 2s. Xia, Xia, Seberry and Wu's Theorem 4 combines it with published base sequences of total length parameter t, where the two distinct sequence lengths are (t+1)/2 and (t−1)/2. The result is four suitable negacyclic matrices of order st. Finlayson and Seberry's Theorem 4 gives the ordinary Hadamard order 4st = (Q+1)t. The original comparison missed the even block sizes s in these rows. [Balonin and Đoković, Proposition 8](https://arxiv.org/pdf/1508.00640#page=13) · [Xia et al., Theorem 4](https://ajc.maths.uq.edu.au/pdf/34/ajc_v34_p105.pdf#page=10) · [Finlayson and Seberry, Theorem 4](https://ajc.maths.uq.edu.au/pdf/30/ajc_v30_p319.pdf#page=5)

| Prime Q | Base-sequence parameter t | Earlier orders (in corresponding order) |
|---:|---|---|
| 35,311 | 19, 23 | 670,928 and 812,176 |
| 73,327 | 7, 11, 13 | 513,296, 806,608 and 953,264 |
| 183,151 | 5 | 915,760 |

## Limits and reproduction

Independent checks covered published negaperiodic pairs and their Golay multiples, the Seberry orthogonal-design constructions, ternary signed-group constructions, recent quaternary and real Miyamoto block transfers, Kumar's pinned certificates and the existing construction comparisons for the 38. A future discovery of earlier seed data could change the 29 unresolved rows. For example, a negaperiodic Golay pair of length 2,998 would yield an earlier route to 815,456 if that input can be documented. [Negaperiodic input audit](fill-negative-closure.md) · [Modern transfers and source pins](fill-recent-audit.md) · [Earlier comparison](priority-later.md)

From this directory, running `node fill-historical-rules.mjs` reproduces all 38 verdict rows from scalar inputs. As a separate limited software check, the installed Sage modules supplied by PassageMath 10.5.49 gave no direct hits for the 38 quarter-orders in the Williamson small-case and spin Goethals–Seidel difference-family lookups. `fill-sage-lookup.py` calls only those two catalog routines in existence mode. The program verifies a positive control and the exact number of queried orders. A catalog miss has no bearing on the nine explicit earlier witnesses. [Lookup code](fill-sage-lookup.py) · [Lookup dependencies](requirements-sage-lookup.txt)
