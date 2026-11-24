# Three earlier orders and the ternary-weight screen

Checked November 24, 2026. All three orders below follow from published constructions.

| Order | Substitution |
|---:|---|
| 598912 | Craigen Theorem 6(4), t=2, L=18+17=35 and g=2304, gives 128(70+4608+1). |
| 760992 | The same theorem, t=1, L=10 and g=11880, gives 32(20+23760+1). |
| 952256 | Four complementary binary sequences of length 14878 give order 64(14878+1) by Craigen–Kharaghani Corollary 10. |

Theorem 6(4) requires 2t binary sequences with total aperiodic autocorrelation zero at positive shifts. Each of its t equal-length pairs contributes its length once to L. BS(18,17) gives the first quadruple and a binary Golay pair of length 10 gives the second pair. The complex Golay inputs are 2304 = 2⁸·3² and 11880 = 2³·3³·5·11. For powers 2ᴬ3ᴮ5ᶜ11ᴰ13ᴱ the standard product condition is B+C+D+E ≤ A+min(A,C+E)+1. The second input attains equality. [Craigen, Theorem 6](https://doi.org/10.1016/0097-3165(95)90002-0) · [Complex Golay product theorem and consecutive base sequences](https://arxiv.org/pdf/2401.15381)

For the last row, take one binary Golay pair of each length 26 and 320 = 2⁵·10 to form BS(26,320). Pair this with BS(22,21). Livinskyi’s Theorem 4.7, attributed there to reference K3, multiplies the two length sums when the second base sequence has consecutive lengths. It gives four real complementary words, each of length (26+320)(21+22)=14878. Corollary 10 applies to exactly these four words. [Livinskyi, Theorem 4.7](https://mspace.lib.umanitoba.ca/server/api/core/bitstreams/46d98169-d70f-4d13-b3c7-a657d0ce68e2/content) · [Craigen–Kharaghani, Corollary 10](https://www.academia.edu/52596923/Hadamard_Matrices_from_Weighing_Matrices_via_Signed_Groups)

## Craigen–Kharaghani 1996

Run `node priority-ternary-bulk.mjs` in this directory. It reads all 94 published-candidate ledger rows. For each order H it tests each T=H/2ʲ divisible by four, all MN dividing T/4, and divisors h of M and k of N. Seed orders are restricted to 1, 2 and multiples of 4, and (2,2) is excluded by the argument in audit-golay.md. Composite seed orders can carry a proper factor of the target odd part. If a seed carries the whole odd part, its ordinary Hadamard matrix already implies H by doubling, so that tautological case is omitted. The screen matches both expressions of Theorem 13 and all nine of Theorem 20, granting every nonnegative weight generated multiplicatively by 2,5,13,17,29 and the empty pair of weight zero. Theorem 13 uses one seed. Theorem 20 uses two. [Theorems 13 and 20](https://ajc.maths.uq.edu.au/pdf/13/ocr-ajc-v13-p89.pdf)

**81 of the 94 have no arithmetic substitution** within this screen. The 13 with a substitution are 119920, 229552, 239840, 399472, 459104, 479680, 486592, 699872, 757360, 760992, 811120, 902240 and 917680. None supplied a further concrete old order under the sufficient packing and seed checks below. The 760992 closure above instead uses the 1995 theorem.

The sufficient test packs disjoint pairs in successive intervals, using multiplicative (weight,span) from (1,1), (2,2), (5,6), (10,10), (13,14), (17,21), (26,26) and retaining the shortest resulting span for each weight. It admits the trivial one-member seed from any ordinary matrix certified here by small-order existence through 1000, prime Paley, or doubling, the (4,2) seed, the square seed of Corollary 18, and tensor products of these. For example at 902240, H(22556) would provide the seed for H(4·22556·10) with weight 8. The seed has odd part 5639 and needs independent construction. At 119920 the first weight partition is 1250+28730=29980. The arithmetic match does not pack the supports. Interleaving different pairs, additional seeds, later primitive weights, transformations beyond Theorems 13 and 20, and transfers other than doubling could give more. [Seed and packing theorems](https://ajc.maths.uq.edu.au/pdf/13/ocr-ajc-v13-p89.pdf) · [Later ternary pairs](https://doi.org/10.1016/j.jcta.2005.07.013)
