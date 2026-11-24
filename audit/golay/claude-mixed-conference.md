# Mixed conference sizes and three certified larger powers

The two-factor Turyn expression with core dimensions a,b has row sum b−a. Multiplying each of its three summands by a phase cannot fix this: the two diagonal contributions must cancel, hence the row sum has modulus |b−a|. In the odd cyclic-string formula let factor j have dimension n_j>1. Restrict the Gram to the tensor product of the constant space at j and its orthogonal complement at every other position. The only surviving word has J at j, I at j−1 and W everywhere else. Its Gram eigenvalue is n_j² times the product of n_k for k outside {j−1,j}. The required core Gram has eigenvalue the product of all dimensions. Thus n_j=n_(j−1) for every j. Rephasing words preserves their individual Gram. These obstructions apply to direct substitutions in the paper's formulas. They do not exclude a different product construction.

For a Hermitian quaternary conference Q of order c, the array with block rows (Q,Q+iI) and (Q−iI,−Q) is Hermitian quaternary conference of order 2c. The off-diagonal block of its square vanishes by commutativity, and each diagonal block is 2Q²+I=(2c−1)I. Iteration from a Hermitian Paley conference of order p+1 (multiply a real skew one by i when necessary) gives input size 2^e(p+1). I intersected the resulting Kumar order 4m, where m=2^(e+1)(p+1)−1 and m−2 is prime, with the local open-odd-parts table through 2999. No match occurs for e≥1 and odd prime power p. The two released non-Hermitian cores have no direct substitution into this doubling proof.

For each of the verified dimensions n=141,321, an exponent sweep through 300 identified the following new entries above exponent 16. Each gives real order 4(2n^r+1) by the released Theorem A.

| n | r | digits of q=2n^r−1 | certificate parameter P |
|---:|---:|---:|---:|
| 141 | 129 | 278 | 10 |
| 141 | 166 | 358 | 4 |
| 321 | 261 | 655 | 10 |

Run `gp -fq claude-conference-primes.gp` in this directory. Write M=q+1 and work modulo q in the algebra x²−Px+1=0. The code verifies gcd(P²−4,q)=1, x^M=1, and for each distinct prime p dividing M, the gcd of q with both coefficients of x^(M/p)−1 is 1. At every prime divisor ℓ of q, x therefore has order M in the quadratic algebra over F_ℓ. If the polynomial splits, its roots belong to F_ℓ and their orders divide ℓ−1. If irreducible, the Frobenius sends x to its reciprocal, so its order divides ℓ+1. Hence ℓ≥M−1=q and q is prime. This is an unconditional existence certificate, without a historical novelty determination. These orders use the paper's theorem unchanged.

## Independent Golay array with a larger fill

Let W be the real pre-fill array with 4N block rows and signed permutation blocks of degree four. Its Gram is 4NI. For any real Hadamard matrix F of order 4k, the product (W⊗I_k)(I_(4N)⊗F) has every block a signed row permutation of F. Its Gram is 16kNI. This proves the proposed formula even if there are extra identities in the concrete representation beyond the formal signed group algebra. Arbitrary-size real monomial representation expansion is classical. [Craigen 1995](https://doi.org/10.1016/0097-3165(95)90002-0) · [Theorem 2.3, explicit restatement](https://doi.org/10.1016/j.disc.2019.111795)

For the 38 orders in the bounded fill sieve, I granted each earlier 1992 pair length every value in {1,3,5} times a binary Golay number, independently for the two inputs. For each target L I enumerated all d dividing L/16 and checked whether s=L/(16d) is a sum of two granted lengths. Every successful s was at most 34, so H(4s) exists. Any old H(4d) usable for that fill would therefore already account for L by the Kronecker product. The only successful s at 125360 was 5 (fill H(6268)), and at 207696 it was 3 (fill H(17308)). Likewise an older degree-two pre-array giving H(8s) and fill H(4d) produces H(16ds) by Agaian's existing product. The 1992 test is bounded to the stated length supply. [Kharaghani 1992, Theorems 6 and 9](https://ajc.maths.uq.edu.au/pdf/6/ocr-ajc-v6-p293.pdf)
