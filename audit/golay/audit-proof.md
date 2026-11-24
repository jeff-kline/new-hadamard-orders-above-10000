# Cold examination, proof and certificate audit

**Verdict. VERIFIED for the universal implication and the three concrete ordinary Hadamard matrices.** A provenance correction to the accompanying material is recorded below. I did not investigate historical priority or certify a frontier table.

## The argument

I checked the construction in mixed-proof.md against the sealed initial derivation. The signed 2-by-2 rotation and reflection matrices satisfy all the dihedral relations, and transpose acts as the source involution. The two embeddings in different tensor factors commute coefficientwise across factors. Within each pair, the requisite commutations are polynomial identities, so substituting the bilateral cyclic shift, including its inverse in the adjoints, preserves them. Reflection on the time index negates exponents. Conjugation by the two coefficient reflections together transposes every allowed letter, covering the real and both non-real possibilities with either sign. No assumption of coefficientwise commutation within one source pair has entered.

I multiplied the displayed block array against its transpose. For example, the first two rows give (AB−BA)J+CD−DC, and the next pair of distinct rows gives BCᵀ−CᵀB+(ADᵀ−DᵀA)J. The simultaneous cyclic permutation of the three outer indices after the first and of B,C,D generates all six row products. Every diagonal sum reduces by normality to the concatenated norm, equal to 4NI by sign cancellation. In each outer slot every position has precisely one signed permutation coefficient, even after applying a transpose and reflection. The final right factor preserves the sign-matrix property at every scalar position and multiplies the Gram by four. These observations discharge the argument for arbitrary positive admissible lengths.

I transcribed the underlined signs of the three source pairs of lengths 7, 9 and 15 directly from the rendered page 142. A separate dense two-by-two matrix convolution in the project-specific environment checked all ordered starred commutators (16 including trivial and reverse checks), and both sides of each aperiodic Gram identity coefficient by coefficient on these three pairs. The real selectors in Lemma 3 choose signed copies of a source word at every block, hence preserve the restricted alphabet. The first two order applications have all-dihedral proofs independent of the complex alternative used in the oracle. The third uses a complex length 11 explicitly listed on p. 141 and tested in the oracle. I compared the source with the printed input strings and inspected the actual seeded multiplications.

**Source erratum.** On page 141 the first binary word in the row headed 26 reads `++++-++--+-+-+--+++--+++`, of length 24. The implementation uses `++++-++--+-+-+--+-+++--+++`, of length 26, and verifies it together with the listed second word. The two additional symbols are +− between the length-16 prefix and the last eight characters. Thus the phrase “all printed binary seeds” should distinguish the executable length-26 input from this incomplete printed string. This difference affects source attribution only. [Original scan, p. 141](https://ajc.maths.uq.edu.au/pdf/18/ocr-ajc-v18-p139.pdf#page=3)

## The checkers

I traced signed-permutation multiplication (composition of the one-based signed column maps), inversion, tensor indexing, Sylvester parity and the cyclic reflection conventions. The time reflection actually used has t ↦ −t. The antidiagonal t ↦ −1−t in the original paper also inverts the shift. The order-160 dense control, its altered-sign negative control, and the separately checked sign oracle address the two indexing conventions.

For the compressed checker, evaluating a cyclic matrix polynomial at B modulo B^N−1 preserves sums and products. Each cyclic coefficient of a given scalar residual has magnitude at most 8N by the four monomial summands and the subtracted diagonal. The chosen B exceeds 16N. The absolute evaluation of a residual is strictly smaller than the modulus, and successive reduction modulo B forces all signed digits to vanish. The complex-sequence check uses ordinary integer evaluation with residual coefficients bounded by 4N and base strictly larger than this bound, which likewise yields uniqueness by successive reduction. The real signed block test separates the two reflection parities, a sufficient condition including at the principal and order-two characters where this expression need not be unique. The direct dense checker and the scalar checker fill every Hadamard coefficient with the same convention prescribed by the proof.

For the scalar checker I traced bit packing, positive and negative rotations by four-bit positions, last partial byte handling, the expected Hamming distance and the target diagonal. For two fixed row types, the residual depends on two correlations as F(j−i)+G(j+i), since a common block either has equal or opposite shift orientations. The complete i=0,1 comparisons force G(t+2)=G(t), making the residual zero for any i. The proof covers both odd and even cycle lengths. This checker depends on the same deterministic entry oracle and analytically checked cyclic-shift covariance. Its Hamming-distance identity computation is independent of the packed Gram checker.

With Python 3.10.3 in an isolated virtual environment (validated unequal sys.prefix and sys.base_prefix), both default checks exited successfully. The compressed checker passed for 160, 25072, 46192, 47968 (8.55 user + 0.03 system CPU seconds). The scalar check passed at all four orders (24.56 user + 0.05 system CPU seconds). The large scalar comparison counts were 802304, 1478144 and 1534976. Independent dense seed checking consumed 0.12 CPU seconds. All used one core, in succession. Assertions were enabled. The workload fits the allocated 120 CPU seconds and six minutes wall.

## Additional claims and exposure

For the single-factor obstruction, I checked the odd-cycle splitting into distinct conjugate characters, the degree bound N−2 for the unshifted cross-commutators, and all 36 cross-ratio products for each of (7,9) and (7,15) over F₂, with no equal products. The spectra and commutant arguments in the final three paragraphs concern the stated restricted embeddings. They do not yield general lower bounds for real Hadamard orders. I have no defect to report in those arguments.

Initial report SHA-256: 576e0442af2c97c486f7e563a9e3680b3f7304ef93632156fb556d801b1e96db. Proof-audit snapshots (SHA-256):

    ee1981fab7d0e6609074fe8809f3192cb6d57e1fb653dfbfc6caaf60ba5d0c2f  mixed-proof.md
    d8c3eff1599b955d94f3a7342c37a61f63ccc2de6695e277487e5082d07939f2  mixed_entry.py
    f5e4d5defc99903073fb0776608521cbdd43c5f128ede8fc25c2ac704065c9cf  check_scalar_rows.py
    cfdb25c64133e3cecb5232cb3f5de3d0fdfa23704a86efb04990c153ee8713d3  mixed_entry.md
    5c4ed98fe848285d15b13af0c9a68409016f551b211a1e2b2ccc2a916e4185e0  README.md
