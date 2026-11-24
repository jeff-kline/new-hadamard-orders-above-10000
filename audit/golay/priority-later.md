# Later tables and quaternary inputs

Six of the 94 candidate rows have earlier constructions by the quaternary and conference methods below. They come from four smaller ordinary matrices. Here WT(w) denotes a Williamson-type quadruple of order w. The Miyamoto II step needs symmetry of the quaternary input. [Egan, Kotsireas, London and Ó Catháin, Tables 3–4 and Remark 8](https://arxiv.org/html/2610.27175v1)

| Target | Earlier ordinary matrix | Construction of its input | Final operation |
|---:|---:|---|---|
| 193712, 387424, 774848 | 96856 | Symmetric BH(3026,4) gives WT(6053). Seberry–Yamada gives H(8·12107). | One, two or three doublings. |
| 394336 | 98584 | BH(12322,4) gives H(8·12323) by complex Miyamoto. | Two doublings. |
| 757360 | 75736 | Symmetric BH(2366,4) gives WT(4733). Since 9467 = 2·4733+1 is prime, Seberry–Yamada gives H(8·9467). | Agaian with H(20) gives 75736·20/2. |
| 996448 | 249112 | Symmetric BH(7784,4) gives WT(15569). Since 31139 = 2·15569+1 is prime, Seberry–Yamada gives H(8·31139). | Two Sylvester doublings give 4·249112. |

For the first two rows, Paley at the prime power 27 supplies skew H(28). Skew doubling gives orders 56 and 112. Turyn's conference construction gives symmetric conference matrices of orders (56−1)²+1=3026 and (112−1)²+1=12322. Adding iI supplies the stated symmetric quaternary matrices. The first chain uses the primes 6053 and 12107. The second uses the prime 12323 congruent to 3 modulo 4 and the unrestricted quaternary Hadamard input of order 12322. [Đoković–Seberry, §2, Turyn C-series](https://us.ticmeet.com/assets/archivos/d6f1d9b8-d39f-4888-925a-7eb81c4905cc/jenni-paper.pdf) · [Kumar's complex Miyamoto transfer](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/hadamard/COMPLEX_MIYAMOTO.md)

For order 757360 take q=1181, a prime congruent to 5 modulo 8. A skew matrix of order (q+3)/2=592 exists by doubling the known skew order 148 twice. The proof of Kumar's Theorem B constructs a **symmetric** BH(2(q+2),4) before passing to the real matrix, and Kumar explicitly lists v=q+2=1183 among the applications. This supplies order 2366. Primality of 4733 and 9467 gives the two transfers in the table, and Paley I at 19 supplies the final H(20). [Kumar, §4 and the discussion of 1183](https://generalised.si/research/skew-symmetric-hadamard) · [Egan et al., Tables 3–4](https://arxiv.org/html/2610.27175v1)

For order 996448, Paley at the primes 13 and 277 gives real symmetric conference matrices of orders 14 and 278. If C is one of these matrices, C+iI is symmetric and its Gram matrix is C²+I. Tensor the resulting BH(14,4) and BH(278,4) with the symmetric real Hadamard matrix of order 2. Their product has order 2·14·278=7784. The odd parameters 15569 and 31139 are prime. The use of symmetric quaternary tensors to supply Miyamoto inputs also predates this search. [Kumar, Miyamoto inputs at a pinned commit](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/hadamard/MIYAMOTO_BLOCKS.md) · [Paley conference construction and C+iI](https://www.cs.uleth.ca/~zaitsevv/quaternary.html)

## Numerical tables

In Seberry–Yamada (2020), Table A.7 lists the two Miyamoto construction rules. Table A.17 is the numerical ordinary-order index, ending at odd part 2999 on p. 293. Table 11.2 additionally gives selected odd parts below 4000. The only candidate below that latter cutoff is 199616=64·3119. The lowest displayed exponent at 3119 is 7, which supplies order 399232. The 2017 *Orthogonal Designs* Appendix A concerns orthogonal designs in the listed orders. [Seberry and Yamada, Appendix A and Table 11.2](https://dokumen.pub/hadamard-matrices-constructions-using-number-theory-and-algebra-9781119520245-9781119520276-9781119520139.html) · [Seberry, 2017 contents](https://documents.uow.edu.au/~/jennie/WEB/WEB17/2017_Bookmatter_OrthogonalDesigns.pdf)

## Conditional orders and scope

The sibling draft lists 159052 and 824332 in the window; adjoining both to the older construction closure gives no candidate row. Its treatment of 4(4q²+3) as a general family would incorrectly remove 179824, 399472 and 506992 by two doublings at q=53,79,89. EKLO Theorem 7 needs four group-developed sign arrays satisfying a particular correlation identity and compatible borders. Section 4 constructs examples for q=19,23. No witness for the three larger values was located. [EKLO, Theorem 7 and §4](https://arxiv.org/html/2610.27175v1)

For prime odd part p congruent to 7 modulo 8, Kumar's complex Miyamoto construction gives H(8p) from BH(p−1,4). For prime q=(p−5)/2, his quaternary Yamada–Kiyasu construction in turn gives BH(p−1,4) from a quaternary conference matrix of order (p+1)/4. Trial division over the 94 candidate rows leaves 21 rows, at the following 13 distinct (p, required conference order) pairs. None of these input orders belongs to the baseline symmetric conference, skew-Hadamard, or prime-power-plus-one supply. [Complex Miyamoto](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/hadamard/COMPLEX_MIYAMOTO.md) · [Kumar, quaternary Yamada–Kiyasu](https://generalised.si/research/hadamard-matrices)

| p | Conference order | p | Conference order |
|---:|---:|---:|---:|
|4327|1082|20287|5072|
|4759|1190|20743|5186|
|6343|1586|28807|7202|
|6607|1652|36871|9218|
|10567|2642|51487|12872|
|13063|3266|||
|14983|3746|||
|17167|4292|||

Allowing every BH(2m,4) with m odd and 2m<2000, then applying realification, complex Miyamoto and the baseline product closure, would reach the three rows 119920, 239840 and 479680 via a conjectural BH(1498,4). Zaitsev lists 1498 among the still missing orders. Jedwab and Pender's 2025 quaternary Legendre families give binary orders 2(q+1) and 4(2r+1), with q a prime power congruent to 1 modulo 4 or with r and 2r−1 prime and prime power respectively. Neither they nor the individual 2026 Legendre lengths 42,46,52,58,64,66,72,80 yielded a target in the baseline product closure. These finite source comparisons leave historical priority unresolved for the other rows. [Zaitsev's table](https://www.cs.uleth.ca/~zaitsevv/quaternary.html) · [Jedwab and Pender](https://arxiv.org/abs/2408.08472) · [2026 lengths](https://arxiv.org/abs/2609.04589) · [Length 64](https://arxiv.org/abs/2609.25573)

## Reproducible propagation from the 2025 census

Run `node family-million.mjs --later --trace-later 2366 4733 75736 7784 15569 249112` from this directory. The candidate file contains the original 94 rows. The checker adds positively recorded inputs before applying the ordinary closure. It takes every 4v in the 2025 census for odd v below 2500, with 655 positive symmetric rows and 513 positive skew rows. The dataset stores odd parts. These totals agree separately with the final cumulative counts in §§2–3. The positive lists were checked against the paper's series and sporadic lists and against the complements of the pinned transcriptions of its two undecided lists. For v=1887 the XXSW series applies directly since 4v−1=7547 is prime and congruent to 3 modulo 8. [Đoković–Seberry, 2025 census](https://us.ticmeet.com/assets/archivos/d6f1d9b8-d39f-4888-925a-7eb81c4905cc/jenni-paper.pdf) · [Pinned symmetric census transcription](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/search/data/symmetric_census_undecided.txt) · [Pinned skew census transcription](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/search/data/skew_census_undecided.txt)

The checker applies Kumar B for every prime power q congruent to 5 modulo 8 whose skew input (q+3)/2 occurs in the supply, and retains the intermediate symmetric BH(2(q+2),4). It also propagates the explicitly added 2025–26 symmetric and skew inputs, skew doubling, Kumar A and D, symmetric real and quaternary tensors, symmetric realification, Miyamoto II, Williamson products, Cooper–Wallis, Seberry–Yamada, complex Miyamoto and the ordinary multiplication and doubling rules. All marked output orders are at most one million. Traces print the supporting input type, which distinguishes a symmetric BH from an unrestricted BH of the same order. [Kumar's theorem statements](https://generalised.si/research/skew-symmetric-hadamard) · [Repeated-block transfers](https://github.com/vatskishan03/Hadamard/blob/d885022144ba6bf4efa8315e14871a3736947527/hadamard/MIYAMOTO_BLOCKS.md)

The later-source branch stabilizes after five passes and accounts for the six rows listed above. The command `node family-million.mjs --later --priority` alternates that branch with the signed-group and complementary-sequence checks and feeds its expanded Williamson supply into those checks. The joint fixed point accounts for nine of the 94 rows, adding 598912, 760992 and 952256 from the other methods. Both executions exclude the candidate family's own matrices as inputs.
