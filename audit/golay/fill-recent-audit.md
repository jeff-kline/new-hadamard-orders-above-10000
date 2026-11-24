# Recent construction and negacyclic multiplication audit

Six of the 38 proposed orders follow from published results available by 2015. The multiplication needed here was proved in 2006. The three Paley primes below supply the inputs. The original 38-row screen allowed circulant Paley blocks only at odd block size. Each of these six uses an even block size. At order 125360 the same search gives no earlier construction.

| Ordinary order | Prime Q | s = (Q+1)/4 | Base-sequence sum t | Order 4st |
|---:|---:|---:|---:|---:|
| 513296 | 73327 | 18332 | 7 | 513296 |
| 670928 | 35311 | 8828 | 19 | 670928 |
| 806608 | 73327 | 18332 | 11 | 806608 |
| 812176 | 35311 | 8828 | 23 | 812176 |
| 915760 | 183151 | 45788 | 5 | 915760 |
| 953264 | 73327 | 18332 | 13 | 953264 |

## Published construction

1. Each prime Q is 3 modulo 4. The Paley negacyclic conference matrix of order Q+1 gives a binary negaperiodic Golay pair of length (Q+1)/2 = 2s. Reading its two sequences as first rows gives two suitable negacyclic matrices of order 2s. Suitability is the Gram identity AAᵀ+BBᵀ=4sI. [Balonin and Đoković, §7, Proposition 8 and equation (10)](https://arxiv.org/pdf/1508.00640#page=13)
2. Put m=(t−1)/2 and use base sequences of lengths m+1,m+1,m,m. All six values of t lie in the odd range through 71 for which Xia, Xia, Seberry and Wu cite these base sequences explicitly. Their Theorem 4 takes the two suitable negacyclic matrices of order 2s to four suitable negacyclic matrices of order ts. The theorem applies to even s. Its additional odd parameter is the difference between the two base lengths, here 1. [Xia et al., pp. 114–115, Theorem 4 and proof of Corollary 2](https://ajc.maths.uq.edu.au/pdf/34/ajc_v34_p105.pdf#page=10)
3. The four matrices have Gram sum 4tsI. The negacyclic Goethals–Seidel array produces H(4ts). [Finlayson and Seberry, Theorem 4](https://ajc.maths.uq.edu.au/pdf/30/ajc_v30_p319.pdf)

These are direct substitutions in published theorems. The search found no source printing the six numerical orders individually.

## Independent route in Kumar's repository

The public HEAD on 24 November 2026 was d885022144ba6bf4efa8315e14871a3736947527. Kumar's proof of Theorem D, §8, puts the Paley matrix of order Q+1 into sixteen negacyclic blocks of order s for every prime power Q ≡ 3 mod 4, including Q ≡ 7 mod 8. Steps 4 and 5 specialize to T-matrices of order 3 to obtain skewness. The intermediate ordinary construction works for arbitrary circulant T-matrices of order t. For block entries N_kj put A_j = Σ_k T_k ⊗ N_kj. Their entries are signs because the T-matrices partition the support. The Paley block-row identities give

    Σ_j A_j A_jᵀ = Σ_{k,l} T_k T_lᵀ ⊗ Σ_j N_kj N_ljᵀ
                  = 4s Σ_k T_k T_kᵀ ⊗ I = 4st I.

The algebra of circulant tensors with negacyclic blocks is commutative and closed under transpose. Reversal on the first factor and back-diagonal reversal on the second implement transpose by the same involution for every A_j. These are exactly the identities for Goethals–Seidel. The six small T-matrix orders also follow by Turyn's base-sequence construction. The six earlier orders therefore persist independently of any new assertion about the dihedral fill. [Kumar, §8 summary](https://generalised.si/research/skew-symmetric-hadamard) · [Kumar, pinned proof, steps 2, 4 and 5](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/skew/PALEY_SKEW.md)

## Other screens and limitations

The companion script checks every row, factors its odd part, tests the two direct Paley negaperiodic series and all known consecutive base-sequence sums through 71. It also tests the direct parameters of Schmidt–Tan Corollary 6.3 for potential ordinary factors carrying the largest odd prime. The normal relative difference set with parameters (2m,2,2m,m) supplies H(2m). For an Agaian lift to N a possible factor d divides 2N and the other input has order 2N/d. The only nonempty outputs of this screen are the Paley factors 35312, 73328, and 183152. In the six relevant rows their cofactors N/d are odd primes, and 2N/d is 2 modulo 4. Classical negacyclic multiplication supplies the necessary odd multipliers. [Schmidt and Tan, Result 1.1 and Corollary 6.3](https://www3.ntu.edu.sg/home/Bernhard/Publications/pub/QuaternionRDS.pdf)

At 125360 = 16·5·1567 the quaternary Miyamoto route at p=1567 would require BH(1566,4) to give H(8·1567). Agaian multiplication with H(20) would then give the target. Zaitsev explicitly lists 1566 among the unresolved orders on 4 November 2026. The two Paley sources for the stronger block form fail at 1565=5·313 and 3131=31·101. Across the 38 rows the largest prime p in every odd part occurs once, is 3 modulo 4, and the complementary odd factor is at most 31. Neither p−2 nor 2p−3 is a prime power for any of these 21 primes. Kumar's two stated Paley inputs for quaternary block multiplication consequently fail when the large prime occurs in the field parameter. If it occurs in the T-matrix input, the possible odd field parameters are at most 31 and already have Williamson-type matrices, so Cooper–Wallis would already cover the same result from that T-matrix. The real Miyamoto block construction has field parameter 1 modulo 4, likewise restricted to the small divisor in these rows. Other quaternary input constructions can change these conclusions. [Zaitsev's quaternary order list](https://www.cs.uleth.ca/~zaitsevv/quaternary.html) · [Kumar, quaternary Miyamoto blocks](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/hadamard/QUATERNARY_MIYAMOTO_BLOCKS.md) · [Kumar, real Miyamoto blocks](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/hadamard/MIYAMOTO_BLOCKS.md)

The 38 rows were selected after the existing million-order closure across the recorded Kumar frontier, its individual certificates, Du–Jiang arithmetic and its subsequent complementary-quad and product transfers. EKLO's October list stops at 10000. Its constructive theorem for bordered arrays requires a certified group-developed core. Only the odd parameter 53 in 899120 = 16·5·(4·53²+3) arises from testing divisibility by 4q²+3 with odd q>1 in these rows. EKLO gives examples at 19 and 23, not 53. No additional certificate for 53 was located. These comparisons do not settle historical priority for the remaining orders. [Earlier bounded closure](priority-later.md) · [Du–Jiang](https://arxiv.org/pdf/2401.15381) · [EKLO, Theorem 7 and §4](https://arxiv.org/html/2610.27175v1)

Run `.venv/bin/python fill-recent-check.py` from this review directory.

As a propagation check, I also reran the existing joint fixed point in a scratch copy of the million-order checker. Before its first ordinary propagation I added H(4tgb) for all its recorded T-matrix orders t, binary Golay lengths g, and b for which 2b−1 or 4b−1 is an odd prime power. I also added H(8tq) for its T-matrix orders and primes q ≡ 3 mod 4 with q−2 or 2q−3 prime. The first extension uses Paley negaperiodic pairs, binary Golay multiplication and the commuting-block proof above. The second uses Kumar's explicit quaternary Paley block inputs. All output orders were at most one million and the candidate fill matrices were excluded as seeds. The joint ordinary and structured propagation reached precisely the same six entries among the 38. The scratch output was checked row by row.
