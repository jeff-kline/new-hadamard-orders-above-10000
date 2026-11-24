# Earlier orthogonal-set constructions at the 38 fill orders

The broadened Craigen–Kharaghani screen found no earlier matrix for these orders. At 125,360 every arithmetic match in the screen requires an ordinary H(6268). That matrix alone, together with Paley H(20), would give the target by Kronecker multiplication. The sequence lengths and supports impose no further obstacle to this conditional route. [Craigen and Kharaghani, 1996, pp. 96–101](https://ajc.maths.uq.edu.au/pdf/13/ocr-ajc-v13-p89.pdf)

I enumerated all seed orders M, N dividing a dyadic predecessor D/4, omitting seeds whose ordinary Hadamard matrices already imply the target by doubling. In the proof after Theorem 20 the available orthogonal sets have sizes 1, h, k, hk. When both h and k are even the paper also obtains size hk/4. The supplementary screen lets any of these sizes occur in each slot of Theorems 10–12 and permits repeated slots and omission of either monomial group. This deliberately grants extra combinations. It checks the numerical forms L=tw+a+b and L=tw+sv and requires contiguous packing in separate intervals using the spans in the checker. The weight-29 pair of length 23 can be made disjoint in 46 positions by spreading the words into even and odd positions. This doubles all differences and preserves complementarity. Shorter or interleaved packings could change the outcome. [2006 paper, Table 4](https://doi.org/10.1016/j.jcta.2005.07.013) · [Run the supplementary checker with Node](fill-signed-audit.mjs)

For 36 targets, every packed match has L≤34. An ordinary H(4L) exists in this range, so any genuine seed at M and N already supplies the target via H(M)⊗H(N)⊗H(4L) and doubling. This argument covers any historical choice of seed matrices for these packed matches. The two larger matches both concern Theorem 20(8).

| Target | Required seed | Sequence input and order |
|---:|---|---|
| 576336 | (12,6) | Six disjoint pairs of binary Golay weight 2000 in length 12007, giving 4·12·(6·2000+6+1). This seed is impossible by the argument below. |
| 727088 | (116,58) | Fifty-eight disjoint pairs of binary Golay weight 26 in length 1567, giving 4·116·(58·26+58+1). The seed remains unverified. |

Here 2000=2·10³. Disjoining a binary Golay pair uses its half-sum and half-difference. Successive disjoint intervals suffice for these two parameters. Each uses the other seed (1,1).

## A necessary condition for a seed of order twice its size

If (2k,k)-seed matrices exist, then k is a sum of two integer squares. Here is a direct proof. Write n=2k and let H and the Qᵢ be the seed matrices as defined on p. 98. The row spaces of the Qᵢ are mutually orthogonal. The identity ∑QᵢQᵢᵀ=nkI forces the sum of their ranks to be at least n, so the sum equals n. Factor each QᵢQᵢᵀ as VᵢVᵢᵀ with Vᵢ having exactly rank(Qᵢ) columns. Concatenating the Vᵢ gives a square matrix V with VVᵀ=nkI. Thus VᵀV=nkI and every positive eigenvalue of QᵢQᵢᵀ equals nk. Its trace n² gives rank two.

The rows of a rank-two sign matrix are, up to sign, two independent words u,v. Indeed a sign word αu+βv requires both α+β and α−β to be signs. Sign-normalize and group the rows. If u occurs r times, the two-dimensional Gram matrix on the normalized group indicators has diagonal rn,(n−r)n and off-diagonal √(r(n−r))〈u,v〉. Both eigenvalues equal nk, so r=k and u,v are orthogonal.

Now QᵢHᵀ is symmetric. Simultaneously permute and sign its rows and columns according to the preceding grouping. Its rows are constant within each group, so symmetry makes the matrix a two-by-two block array with constant integer blocks. All block values are even because they are signed dot products of even-length sign vectors. Call the top two values a,b. The square of the matrix is conjugate to nQᵢQᵢᵀ. Comparing a diagonal entry gives k(a²+b²)=n², or k=(a/2)²+(b/2)². This rules out k=6, since squares modulo three are zero or one and 9 does not divide 6. For k=58 the required values have absolute values 6 and 14, since 58=3²+7². The necessary condition supplies no seed.

This historical audit concerns the specified ternary and orthogonal-set inputs. The existing comparison separately covers Craigen’s 1995 binary representation transfers and Kharaghani’s 1992 block lengths. The resulting evidence supports no claim of worldwide priority. [Earlier signed-group comparisons](priority-methods.mjs) · [Earlier block-length analysis](claude-mixed-conference.md)
