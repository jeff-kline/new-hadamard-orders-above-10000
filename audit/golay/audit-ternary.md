# Can the ternary complementary pair construction give order 47,968?

The weight identity $125+2873=2998$ meets the numerical equation in Craigen–Kharaghani Theorem 20(9). The published factors give a complementary pair of each weight. To obtain order 47,968 this way requires a placement of both pairs on the same 2998 coordinates that covers each coordinate exactly once. The journal's ordinary block products of the representatives examined below fail even after cyclic wrapping. I found no published packing at this length. This leaves the possibility of different representatives or a different construction open.

## What the theorem requires

Theorem 20 assumes seed matrices of types `(M,h)` and `(N,k)`. Part 9 applies Theorem 12 to `h+k` pairs of ternary sequences, with `h` pairs of weight `w` and `k` of weight `v`, all of length `L=hw+kv`. The conclusion has order `4MNL`. The definition on p. 91 requires all `2(h+k)` component sequences to have mutually disjoint supports. Each pair has constant summed Laurent norm, the nonperiodic condition (pp. 90–91). Since the total number of nonzeros equals the specified length, the supports partition the coordinates. For `M=N=2, h=k=1`, each singleton seed set can consist of its Hadamard matrix itself. [Craigen and Kharaghani, definitions, Theorems 12 and 20(9)](https://ajc.maths.uq.edu.au/pdf/13/ocr-ajc-v13-p89.pdf)

In this example a valid packing would give the stronger order **11,992** directly. The four disjoint sequences would be T-sequences of length 2998. Applying the Cooper–Wallis construction as restated on pp. 91–92 gives an orthogonal design of order $4L$ and type `(L,L,L,L)`. Setting all four variables to 1 gives `H(4L)=H(11992)`. The same observation applies to a valid periodic packing because that construction uses circulant Gram identities. [Craigen and Kharaghani, pp. 91–92](https://ajc.maths.uq.edu.au/pdf/13/ocr-ajc-v13-p89.pdf)

## Known factors and failure of the direct placement

The minimum ordinary TCP lengths for weights 5, 13 and 17 are 3, 9 and 13 respectively. The corresponding pairs may have overlapping components. The 1996 paper supplies disjoint pairs of lengths 6 and 14 for weights 5 and 13. The 2006 authors give a disjoint length-21 representative of weight 17 in Table 4, obtained from their second length-15 pair of that weight in Table 3. The 1996 Theorem 21 multiplies both the weights and the displayed lengths of two disjoint pairs. Thus these particular inputs supply weight 125 at length 216 and weight 2873 at length 4116. The ordinary side-by-side construction takes 4332 positions. Theorem 24 supplies special tight packings for weights 5 and 13 and for sufficiently many copies of certain prime powers. It supplies no packing for this single pair of each composite weight. [Craigen and Kharaghani, pp. 102–103](https://ajc.maths.uq.edu.au/pdf/13/ocr-ajc-v13-p89.pdf) · [Craigen and Koukouvinos, foundational TCP theory](https://www.sciencedirect.com/science/article/pii/S0097316501931899) · [Craigen, Georgiou, Gibson and Koukouvinos, Tables 3–4](https://doi.org/10.1016/j.jcta.2005.07.013)

There is also a lower bound on the **displayed block length** of this straight three-factor multiplication for any disjoint factor representatives. A disjoint pair of odd weight $u>1$ cannot fill exactly $u$ positions. If it did, its sum and difference would be a binary complementary pair of odd length $u$. At cyclic shift one, each binary sequence has an even number of sign changes around the cycle, so its periodic autocorrelation is $u$ modulo 4. The two autocorrelations then sum to 2 modulo 4, contradicting complementarity. Thus a weight-13 disjoint input needs at least 14 positions and a weight-17 disjoint input needs at least 18. Theorem 21's stated product length is at least $14^2\cdot18=3528>2998$. Translation, reduction of individual spans, or periodic folding requires a further check beyond this length bound.

For that check, let `Q` be the printed weight-13 pair `(1110-110-1-000, 0001000-000101)`. Let `R` be `(101-110-0001001 000000, 000000 rev(101-010110--00-))`, with spaces suppressed and `rev` reversing the indicated word. Here a hyphen is a single minus one. This uses the published length-15 pair, a reversal and a six-position relative shift. The supports of each pair are disjoint and direct convolution gives zero summed aperiodic autocorrelation at every positive shift.

The following counts use Theorem 21 literally. For ordered inputs `(U,V)`, `(S,T)`, the two output words are `U⊗S + V⊗rev(T)` and `U⊗T − V⊗rev(S)`. For each output word $X$, the last column counts indices $i$ with both $X_i$ and $X_{i+2998}$ nonzero. The counts agree for the two parenthesizations and for the two output components.

| Factor order | Span of each component | Collisions per component modulo 2998 |
|---|---:|---:|
| Q, Q, R | 4110 | 98 |
| Q, R, Q | 4113 | 114 |
| R, Q, Q | 4113 | 132 |

For example the first output component of `(Q×Q)×R` is nonzero at zero-based positions 5 and 3003. No independent translations or reversals of the final components alter the collision counts. Laurent reduction modulo $z^{2998}-1$ preserves a periodic norm identity, but two nonzeros that land on the same coordinate yield a zero or a coefficient of magnitude two there. The support count drops in either case. Thus these representatives cannot supply the required disjoint ternary inputs by wrapping them modulo 2998.

## Other numerical parameters in Theorem 20

I checked all nine parts with each seed order a power of two and the weights in the multiplicative semigroup generated by 2, 5, 13, 17 and 29, together with the trivial weight 0. This semigroup covers the prime weights in the cited catalogues. A seed order involving the odd prime factor of a target would already require a Hadamard matrix at a divisor of that target carrying the same prime. The table concerns constructions with the prime supplied by the sequence length. [Primitive TCP catalogue and update](https://doi.org/10.1016/j.jcta.2006.09.002)

Two seed restrictions sharpen the count. For an `(N,k)` orthogonal set let $S=\sum C_i$. The defining identities give $SS^T=NkI$. Write $P_i=C_iS^{-1}=C_iC_i^T/(Nk)$. These matrices are symmetric, sum to the identity, and satisfy $P_iP_j=0$ for distinct indices, hence are projections. Their trace is $N/k$, so $k\mid N$. Also `(2,2)` seed matrices would require a rank-one sign matrix $ab^T$ amicable with a Hadamard matrix $H$ of order two. Symmetry of $Hba^T$ forces $Hb=\lambda a$, and norms give $|\lambda|=\sqrt{2}$, contradicting integrality of $Hb$. [Craigen and Kharaghani, equations (3)–(4) and seed definition](https://ajc.maths.uq.edu.au/pdf/13/ocr-ajc-v13-p89.pdf)

| Target | Parts 1–8 | Surviving part 9 arithmetic, up to exchange |
|---|---|---|
| 25,072 | none | none |
| 46,192 | none | none |
| 47,968 | none | one pair of each weight `(125t,2873t)` for $t=1,2,4$, at length `2998t` |

To reproduce the enumeration, let `M,N` range over 1, 2, 4 and 8 with `4MN` dividing the target. Put `L=target/(4MN)` and take `h|M, k|N`, removing the inadmissible `(2,2)` seed type. Generate the stated weight set through 11992 by multiplication. In parts 1–8 solve `L=jw+b` for the eight ordered choices `(j,b)=(1,h+k), (1,h+hk), (h,k+1), (h,hk+k), (h,h+k), (h,hk+1), (hk,h+1), (hk,h+k)`. In part 9 test `L=hw+kv` for each generated weight pair. Each surviving row is an arithmetic condition. In particular, a packing at one of the two larger scaled lengths need not descend to a packing at 2998.
