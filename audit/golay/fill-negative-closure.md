# Negaperiodic Golay inputs and product closure for the 38 orders

The extended screen reproduces the same six earlier constructions as the direct Xia check. It finds no seventh, including at 125,360. Each positive row uses Proposition 8 of Balonin–Đoković for an NG pair of length v=(q+1)/2. Xia et al., Theorem 4, with ordinary base sequences BS((t+1)/2,(t−1)/2), gives four suitable negacyclic blocks of size vt/2, hence an ordinary Hadamard matrix of order 2vt. All six t values lie in the explicit range of Xia et al., Corollary 2(ii). The three q values are primes and are 3 modulo 4. [Balonin–Đoković, §§5–8](https://arxiv.org/pdf/1508.00640) · [Xia et al., pp. 110–115](https://ajc.maths.uq.edu.au/pdf/34/ajc_v34_p105.pdf)

| q | NG length v | t | Ordinary order |
|---:|---:|---:|---:|
| 73327 | 36664 | 7 | 513296 |
| 35311 | 17656 | 19 | 670928 |
| 73327 | 36664 | 11 | 806608 |
| 35311 | 17656 | 23 | 812176 |
| 183151 | 91576 | 5 | 915760 |
| 73327 | 36664 | 13 | 953264 |

Run `node fill-negative-closure.mjs` to check every ledger row. The search uses both Paley lengths, including the stronger halved length, and all products by binary Golay lengths 2ᵃ10ᵇ26ᶜ. Xia’s Theorem 3 already gives this multiplication. It also checks the Whiteman quasi-Williamson length p(p+1), granting prime powers as an upper bound on the prime parameter. All even NG seed lengths up to 2996 are granted, including the complete small example range through 92 and any overlooked sporadic seed in that interval. It grants every doubled candidate complex length supported on 2,3,5,11,13. Egan's Theorem 2.2 and §4 conversion justify the actual subset coming from complex Golay lengths. [Xia, Theorem 3](https://ajc.maths.uq.edu.au/pdf/34/ajc_v34_p105.pdf) · [Balonin–Đoković, §§1, 9](https://arxiv.org/pdf/1508.00640) · [Egan, §§2, 4](https://doras.dcu.ie/31213/1/Phased%20unitary%20Golay%20pairs%20%28pre%29.pdf) · [Executable enumeration](fill-negative-closure.mjs)

The checker grants every odd base length sum through 1497, and the infinite families t=g+1 and 2g+1 for binary Golay g. The first comes from a binary Golay pair plus the trivial pair, and the second from consecutive base sequences. Theorem 4 permits an odd difference between its two base lengths. For t=1 the bare NG pair already gives H(2v). An arbitrary T-matrix by itself does not meet the hypotheses of this theorem.

For each target D, write p for its largest prime factor. The checker tries every H dividing 2D with p dividing H and H divisible by 4. The factor K=2D/H may be 2 or any multiple of 4, which grants all possible Agaian partners and includes doubling and ordinary Kronecker multiplication. If the large prime occurs in K instead, each allowable missing H is at most 272, where all ordinary Hadamard orders divisible by four were already available. Such an H therefore adds no construction. Likewise, if p divides the odd t, a new base sequence or genuine T-matrix of length t would already give H(4t). At a direct target the cofactor 2s, where s=D/(4t), is divisible by four and at most 272, so Agaian already combines H(4t) and H(2s) to give D. [Historical comparison rules](family-million.mjs)

At 815456, the first NG seed outside the generous small interval illustrates the historical limitation. An NG pair of length 2998 would give H(5996) and lead to the target with Agaian partner H(272). This is a conditional construction. The upper search limit of 2996 records where unverified seeds first change the result. No exhaustive claim about all published sporadic NG pairs above that limit follows.
