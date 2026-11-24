# Two independent dihedral Golay pairs give a Hadamard matrix of order 16(m+n)

Let (a,b) and (c,d) be dihedral Golay pairs of lengths m and n in the sense of Kamali and Kharaghani. Each entry lies in {±1,±i,±s}, with i²=−1, s²=1, is=−si. A complex Golay pair satisfies this definition. A pair has complementary aperiodic autocorrelations, and its two Laurent polynomials commute with each other and with both adjoints, including normality. Then there exists an ordinary Hadamard matrix of order 16(m+n). [Kamali and Kharaghani, definition and Theorem 7, pp. 141–143](https://ajc.maths.uq.edu.au/pdf/18/ocr-ajc-v18-p139.pdf)

Represent i by the real rotation through 90 degrees and s by diag(1,−1). Use two independent tensor factors of dimension two. Embed every coefficient g in the first pair as g⊗I and every coefficient h in the second pair as I⊗h. Denote the four resulting polynomials by a,b,c,d. All four and their adjoints commute as Laurent polynomials, by the two within-pair hypotheses and independence of the coefficient factors. Let N=m+n, evaluate at the order-N cyclic shift and put

    A=a+z^m c,  B=a−z^m c,  C=b+z^m d,  D=b−z^m d.

Every coefficient of every concatenation is a signed permutation matrix of size four. Each of the two aperiodic Golay identities survives evaluation on the shift. The sum of AAᵀ, BBᵀ, CCᵀ and DDᵀ is therefore 4NI. The four matrices and their transposes commute pairwise.

Write R for the order-N reversal matrix and put J=R⊗s⊗s. Thus Jᵀ=J and J²=I. Conjugation by J takes each input block X to Xᵀ because reversal inverts the shift and sgs=gᵀ for g=1,i,s and their negatives. This linear equality applies to transposes as well. In Kamali and Kharaghani's array replace their order-2 coefficient reflection by the tensor coefficient reflection:

    A       −BJ     −CJ     −DJ
    BJ       A      −DᵀJ     CᵀJ
    CJ       DᵀJ     A      −BᵀJ
    DJ      −CᵀJ     BᵀJ     A

Each diagonal block of its Gram matrix is 4NI, by the conjugation identity and normality. The first row dotted with the second row gives [A,B]J+[C,D], where [X,Y]=XY−YX; the first-row products with rows three and four cyclically permute B,C,D. The product of the second row with the third is BCᵀ−CᵀB+(ADᵀ−DᵀA)J; the other two products are cyclic permutations up to signs. All are zero. Each position in the coarse 4N-by-4N matrix holds a signed 4-by-4 permutation. Postmultiply by I_(4N)⊗H₄. Every position now holds a sign matrix and the Gram matrix is 16NI. This proves the claim.

The first two applications need only the three published, admissible dihedral seeds of lengths 7,9,15. Kamali and Kharaghani's Lemma 3 extends such a pair to length gt for every binary Golay length t. Its disjoint real selectors place signed copies of the input words and preserve the allowed alphabet.

| Dihedral lengths | Binary Golay multiplier | Ordinary order |
|---|---|---:|
| 7 and 15·104 | 104=2²·26 | 16·1567=25072 |
| 7 and 9·320 | 320=2⁵·10 | 16·2887=46192 |

A third application uses the complex Golay pair of length 11 listed in the same paper, multiplied by the binary length 256. Pair it with the dihedral length 7 multiplied by 26. The resulting lengths 182 and 2816 sum to 2998, giving H(47968)=H(32·1499).

Kumar's frontier records least known exponent 5 for 1567 and 2887, and 6 for 1499. The displayed matrices improve all three records by one exponent. This establishes a comparison with a specific snapshot. The proof above does not adjudicate priority against every earlier construction. [Kumar, frontier](https://github.com/vatskishan03/Hadamard/blob/main/FRONTIER.md)

## What fails in the original, two-dimensional coefficient space

For odd N, the first-row products displayed above show that the *actual block array* requires the original A,B,C,D to commute pairwise at each nonprincipal Fourier frequency. Indeed, a circulant preserves its character space, whereas a circulant followed by J sends it to the conjugate character space. These spaces are different at every nonprincipal character of an odd cyclic group. Splitting the sum into its two destinations forces both parts to vanish, and replacing a character by its conjugate accounts for the reversed term. Taking sums and differences recovers all commutators of ingredients before concatenation. In particular each first-pair polynomial must commute with each second-pair polynomial. Their cross-commutators have degree at most N−2 before reduction modulo z^N−1. Vanishing at all N−1 nonprincipal roots then implies identical vanishing as polynomials. This proves the necessity without assuming that the paper's sufficient conditions were necessary.

For the displayed seeds the first word is real. Write the nonscalar part of the second word as iU(z)+sV(z). Two such second words commute precisely when U₁V₂−U₂V₁ vanishes. The orders at z=0 of V/U are −2, −3, +1 for the words of lengths 7,9,15, respectively. In Lemma 3 the nonscalar parts of both expanded words are scalar-polynomial multiples of the old nonscalar part, and at least one is nonzero. Hence the original coefficient representation fails for the two displayed decompositions. Reversing the words, alternating signs, adding scalar delays, or changing the sign of either coefficient direction does not remedy the unequal valuations because all three symbol supports in each seed are reversal-invariant.

There is also a sign-independent check allowing any permutation of the three symbol classes before binary scaling. The supports of the scalar, i, and s coefficients in the three published words, in that order, are as follows (indices start at zero).

    7   {1,5}          {2,3,4}               {0,6}
    9   {1,2,6,7}      {3,5}                 {0,4,8}
    15  {0,14}         {1,3,5,7,9,11,13}     {2,4,6,8,10,12}

Interpret each subset X as the polynomial Σ_(j∈X) z^j over F₂. For each pair (7,9) and (7,15), the six ratios of two distinct polynomials on the first side have empty intersection with the six ratios on the second. This can be checked by cross-multiplying the displayed polynomials in F₂[z]. A real sign change at any original coordinate does not affect this obstruction. For a genuinely complex companion with nonzero imaginary polynomial V and a seed using s with polynomial W, the corresponding commutator is ±2isWV, which is nonzero. This argument applies to this one-factor spliced array. The existence of a smaller-order matrix by other means stays open.

For a uniform coefficient embedding, i and s generate M₂(R), whose commutant on its natural two-dimensional real representation consists only of scalars. An independent commuting complex unit needs at least two such real modules. The size-four tensor representation attains that bound.

Even a rationally varying complex unit cannot commute identically with the printed length-seven seed. Its nonscalar part iU+sV has U(0)=0 and V(0)=1. At every sufficiently small positive real z its eigenvalues are the distinct real numbers ±√(V²−U²). Any real matrix commuting with it is diagonal in the same real eigenbasis. If a matrix T over R(z) commuted identically with the seed and satisfied T²=−I, specializing at such a z outside its finite set of poles would give a diagonal real square root of −I. This excludes that particular aperiodic embedding even with a rational change of axis.

At odd total length N, allowing an independent complex phase to act on every position at once still fails if it commutes with the entire constant dihedral coefficient algebra. Its action would belong to the commutant I₂⊗M_N(R). An N-dimensional real matrix cannot square to −I when N is odd, by determinants.
