# Proof audit: "New Hadamard orders above 10^4" (draft v0.1.0)

Date: 24 November 2026. Process-separated AI audit of `paper/main.tex` and `code/`. Each argument
was rebuilt by hand; small exact checks were run in a venv (single core, well under 60 CPU-seconds;
scripts `chk.py`, `chk2.py`, `chk3.py`, `chk4.py` in the session scratchpad, not in the release).
This is not independent expert peer review.

Labels: VERIFIED (rebuilt and agrees), ERROR, GAP (argument or check incomplete), DOCUMENTATION
(statement true or harmless, wording or code/paper mismatch), NOT AUDITED (source unavailable).

**Overall verdict: no mathematical error found. Theorems A, B (existence), C and D (existence) are
verified. Seven documentation items and two verification/sieve gaps, none of which changes a
theorem. The two gaps were closed by hand here for the three orders, but the code and text should
be fixed.**

## 1. Lemma 1 (power construction, non-Hermitian cores) — VERIFIED, one DOCUMENTATION item

- r = 2. Diagonal 0·0 + 1 − 1 = 0. Off the diagonal exactly one of Z⊗Z, I⊗J, J⊗I is nonzero
  (both blocks differ / same first index / same second index) and it is a unit. The six cross terms
  of Z₂Z₂* each contain ZJ or JZ* = (ZJ)*, so only ZJ = 0 is used. The remaining terms sum to
  n²I − J⊗J. Line sums: Z₂(1⊗1) = n − n = 0 and (1⊗1)ᵀZ₂ = 0 by JZ = 0. Agrees with the text.
- Odd r. I re-derived Glazyrin's three steps without the Hermitian hypothesis.
  (a) For each 0/1 word L ≠ 1…1 there is exactly one string with W or J at the zeros and I or J at
  the ones (a block of ones is forced to I, J, I, …; a zero is J exactly when its predecessor is I).
  For odd r no string consists of I and J only. This gives zero diagonal and exactly one nonzero
  summand, a product of units, at every off-diagonal position. No symmetry is used.
  (b) Two distinct strings have W against I at some position (otherwise both fit one word L), and
  by the swap-and-reverse symmetry W against J at some position. Hence G_S G_{S'}* contains a
  factor ZJ* = ZJ = 0 or JZ* = (ZJ)* = 0. Only ZJ = 0 is used, as the paper says.
  (c) G_S G_S* is a product of nI − J, I, nJ. The all-I and all-J terms come only from W…W, with
  coefficients n^r and (−1)^r = −1. A mixed term has, cyclically, an I followed by a J; the
  contributing strings pair as (W, W, S′) and (I, J, S′), which are strings simultaneously (both
  require last(S′) ≠ I and first(S′) ≠ J), with coefficients −n and +n. This is pure algebra in I
  and J; W² is replaced by WW* and nothing else changes.
- r = 2^a r′: correct (r′ = 1 is the base core).
- Exact checks: quartic cores of orders 5 and 13; r = 2, r = 3 (order 125), r = 4 by double
  squaring (order 625); all 12 cross products G_S G_{S'}* vanish at n = 5, r = 3.
- DOCUMENTATION. For odd r the proof never says that Z_r has zero row and column sums, which the
  definition of a core requires. One sentence suffices: every string contains W, so
  G_S(1⊗…⊗1) = 0 by ZJ = 0 and (1⊗…⊗1)ᵀG_S = 0 by JZ = 0.
- DOCUMENTATION. The test cores in the Remark (quartic characters of F₅, F₁₃) are skew-symmetric
  (Zᵀ = −Z), so they are non-Hermitian but not generic. The generic case is exercised only through
  random-vector checks on the order-141 and order-321 cores. The hand proof covers it.

## 2. Theorem A — VERIFIED

- n odd gives 2n^r ≡ 2 (mod 4), so q ≡ 1 (mod 4); n^r + 1 = (q + 3)/2. Correct.
- "n odd" is automatic: reducing QQ* = (c − 1)I modulo (1 + i) gives c even for every quaternary
  conference matrix. So the abstract's omission of "n odd" is not an overstatement.
- Kumar's Theorem 3 (CONFERENCE.md §3) assumes only: q prime, q ≡ 1 (mod 4), and any quaternary
  conference matrix of order (q + 3)/2 in normal form. Normal form is free by unit scalings. Its
  text says "No symmetry of Q is used", and I confirmed this by redoing the proof: entries of X′, Y′;
  line sums X′eᵀ = (1 + i)eᵀ, Y′eᵀ = 0; X′Y′ = Y′X′; X′X′* + Y′Y′* = 2vI − 2J using
  ZZ* = Z*Z = nI − J; all border blocks of XX* + YY*, X*X + Y*Y and XY − YX. The proof needs Z*Z
  and zero column sums as well as ZZ* and row sums; these follow from QQ* = nI because Q/√n is
  unitary. No hidden hypothesis. The one external input is Yamada's Lemma 3 (symmetric circulants
  M, N, M² + N² = qI), which the code checks at each q.
- Turyn doubling (Kumar's Theorem 4): re-derived, correct.

## 3. Theorem B and Section 3 — existence VERIFIED; DOCUMENTATION items; one verification GAP

- Table: 141² + 1 = 19882, q = 39761; 321² + 1 = 103042, q = 206081; 141³ + 1 = 2803222,
  q = 5606441. All three q are prime (deterministic Miller–Rabin) and ≡ 1 (mod 8).
  39763 = 17·2339, 206083 prime, 5606443 = 31·223·811. All correct.
- Inputs, exact dense checks: QH566 satisfies KK* = 566I; rows 2–283 × columns 285–566 equal
  J₂⊗Z + P⊗I in full (the release code checks only the upper half of this block); Z is a core of a
  QC(142) and is not Hermitian, skew-Hermitian, symmetric or skew-symmetric. Kumar's C1286 gives a
  QC(322) whose normal core has none of these symmetries either.
- DOCUMENTATION. "has exactly the layout of Lemma 2" is too strong. In QH566 the lower blocks are
  −iY* and iX* (not Y* and −X*), the borders are different units (X border −1 with corner i; Y border
  all 1), and M, N are symmetric, commute and satisfy M² + N² = 281I but are not circulant in the
  file's index order. Only the Y′ block is used, and that part is exact. Suggested wording: "its
  rows 2–283 and columns 285–566 are J₂⊗Z + P⊗I".
- DOCUMENTATION. "random unit vectors": the code uses vectors with independent entries in
  {1, −1, i, −i}, not vectors of norm 1. With those vectors a nonzero defect matrix D gives
  Pr[Dx = 0] ≤ 1/4, so "fails with probability at least 1/2" is correct and conservative (3/4 holds).
  Say what the vectors are.
- GAP (verification, minor). Check (iv) tests K(K̃x) = K̃(Kx) = cx, where K̃ is a separately coded
  routine meant to be K*. That shows K̃ = cK⁻¹, and KK* = cI only if K̃ = K*. Adjointness is tested
  only in the dense controls (orders 38, 198, 1286), not at the three large orders. A randomized
  test ⟨Kx, y⟩ = ⟨x, K̃y⟩ at full size would close this. Theorem B does not depend on it: existence
  follows from Theorem A, the exact input checks and the primality of q.
- Counts in the text (3, 3, 2 vectors; 43 exact lags; negative control) match the code and evidence.

## 4. Section 4 (newness) — stated reasons VERIFIED; one GAP in the sieve; DOCUMENTATION

- 9356 = 4·2339: on the open list used by the code (83 orders 4·odd, matching Kumar's FRONTIER
  count); FRONTIER also has 2339 at exponent 4. EKLO's own Table 5 was not available to me.
- 824332: 206083 is prime and ≡ 3 (mod 4); 824331 = 3·274777; 412165 = 5·13·17·373; Yamada needs
  a symmetric conference matrix of order (q + 3)/2 = 103042 (no skew-Hadamard alternative, since
  103042 ≡ 2 mod 4). 321 = 3·107 is not a sum of two squares, so no symmetric conference matrix of
  order 322 exists and squaring cannot supply one. All correct. Note 103041 = 321² is itself a sum
  of two squares, so existence at order 103042 is not excluded; "none is known" is the right claim.
- DOCUMENTATION. "only Paley's constructions and Yamada's would apply" omits routes that the code
  does test for a prime odd part: Williamson-type matrices or T-matrices of order 206083, Kumar's
  template or Miyamoto's symmetric-quaternary corollary with any QC(103042). List them or say
  "among the constructions tested".
- `openness.py` matches the stated over-approximations for T (≤ 200, families, product closure),
  Williamson-type (odd < 2000), Hadamard below 10^4, and conference cores (≤ 4000, prime power + 1,
  Mathon, Seberry–Whiteman). Its docstring lists T-lengths g + g′ but codes only g′ = 1; for odd t
  this loses nothing.
- GAP. The docstring says every ingredient set is too large. That is false for H(4s) with
  s ≥ 2500: `H4` then accepts only Paley orders and does not recurse. Example: H(4·25141) and
  H(4·6913) are reachable by the sieve's own routes (T(31) × WT(811), T(31) × H(892)) yet `H4`
  returns False. For the three orders I closed this by hand: the only divisor t > 1 with T(t) true
  and cofactor ≥ 2500 is t = 31 at 22425772, and `routes(4·180853)` is empty (Yamada's q = 180851
  is ≡ 3 mod 4). So NOT REACHED stands. Fix: make `H4` recursive, or state the limit in Section 4.
- GAP (bounded). The Williamson-type set above 2000 holds only (q + 1)/2 and q; families such as
  q(q + 1)/2 are absent, and the T set is asserted, not shown, to contain every published family.
  I tested the cofactors 2339, 39763, 206083, 6913, 25141, 180853, 5606443 against the shapes q²,
  q² + q + 1, (q² + 1)/2, q + 1, (q + 1)/2, q(q + 1)/2, 2q + 1 (q a prime power): no hit. This is
  evidence, not a proof that the sets are supersets; the paper's hedged wording ("none of the
  constructions listed reaches them") is appropriate.

## 5. Theorems C and D — VERIFIED; DOCUMENTATION items

- Representation: i ↦ rotation, s ↦ diag(1, −1) satisfies i² = −1, s² = 1, is = −si; sgs = gᵀ for
  g ∈ {±1, ±i, ±s}. It fails for ±is (s(is)s = −is but (is)ᵀ = is), so the restriction of the
  entries in the definition is necessary and is present.
- Commutation: all of a, b, c, d and adjoints commute (within a pair by hypothesis, across pairs
  by the tensor factors; z commutes with coefficients). AAᵀ + BBᵀ + CCᵀ + DDᵀ =
  2(aa* + bb*) + 2(cc* + dd*) = 4N·I. A, …, D have every 4×4 block a signed permutation because a
  and z^m c occupy disjoint shifts.
- Reflection: R z R = z⁻¹ and (s⊗s) acts as transpose on both embeddings, so 𝒥X𝒥 = Xᵀ; hence
  X𝒥 and Xᵀ𝒥 are symmetric.
- Array: all ten block products computed by hand. Diagonal blocks 4N·I (using XᵀX = XXᵀ). The
  off-diagonal blocks are [A,B]𝒥 + [C,D], [A,C]𝒥 − [B,D], [A,D]𝒥 + [B,C], [B,Cᵀ] + [A,Dᵀ]𝒥,
  [B,Dᵀ] − [A,Cᵀ]𝒥, [C,Dᵀ] + [A,Bᵀ]𝒥. All vanish. Fill by I⊗H₄ gives ±1 entries and Gram 16N·I.
  Order 16(m + n). Correct.
- Dense checks built from the paper's text alone: D7 + complex length 3 (order 160), D7 + D7
  (order 224), swapped factors (160): Hadamard. With the plain 2×2 representation, D7 + complex
  length 3 fails (coefficients do not commute), as the paper says; D7 with itself does not fail,
  consistent with "for the inputs below".
- Theorem D arithmetic: 7 + 1560 = 1567, 7 + 2880 = 2887, 182 + 2816 = 2998 = 2·1499; orders
  25072, 46192, 47968 = 32·1499. FRONTIER.md lines 61–62 record exponent 5 for 1567 and 2887 and
  6 for 1499, i.e. 50144, 92384, 95936. Correct.
- DOCUMENTATION (paper/code mismatch). The proof decomposes 1560 = 15·104 and 2880 = 9·320
  (Kamali–Kharaghani lengths 15 and 9). The code builds and checks different inputs: complex Golay
  length 3 times 520 = 2·10·26, and complex Golay length 18 times 160. The release verifies no pair
  of length 9 or 15. Both routes give the orders if the published pairs are as described, but the
  proof should state the decompositions that are checked (3·520, 18·160, and 7·26 with 11·256).
- DOCUMENTATION. The paper cites the array as [KK98, Theorem 7]; the code comment calls it
  Kamali–Kharaghani Lemma 2. Reconcile.
- NOT AUDITED: the text of Kamali–Kharaghani 1998 and Kharaghani 1992 (existence of lengths 9 and
  15, Lemma 3, the amicability hypothesis of Lemma 7), the counts 94/85/9 and the Du–Jiang remark.
  Lemma 3's product does preserve the paper's definition (I checked the identity; the code checks
  the length-182 pair directly). I did not re-run the release's compressed Gram check at the three
  orders (evidence file present).

## 6. Remark on the 16k(m + n) fill — VERIFIED

(W⊗I_k)(I_{4N}⊗F): each 4k×4k block is a signed block permutation of the rows of F, so entries are
±1; Gram = 4k(WWᵀ⊗I_k) = 16kN·I. Dense check with k = 3, F = Paley H(12), N = 10: Hadamard of
order 480. The counts 38/9/29 and the value 125360 = 16·5·1567 were not audited.

## 7. Abstract and introduction — no overstatement found; DOCUMENTATION

- Abstract's Theorem A without "n odd": fine (item 2). Newness claims are hedged consistently with
  Section 4. "Each half the smallest order previously recorded": matches FRONTIER.
- Intro's description of the open list (4p, 4kp with k ≤ 13, 8p) is consistent with the code's list
  plus FRONTIER's six orders 8p; EKLO itself not read.
- Table 2: every exponent list reproduced exactly (r ≤ 16, Miller–Rabin).
- DOCUMENTATION. Section 5: "that would need 2n² + 1 < 2500 … the candidates n = 15 and n = 21".
  With r ≥ 2 and odd n ≤ 35, 2n^r − 1 is also prime for n = 3 (r = 2, 3), 5 (r = 4), 7, 11, 13, 17,
  25. Those n are prime powers and the orders (76, 220, 396, 972, 1356, 2316, 5004) are not open,
  so the conclusion holds, but the sentence should say that 15 and 21 are the non-prime-power
  candidates.
- DOCUMENTATION. Kumar's local CONFERENCE.md copy covers 1286, 1718, 2102, 3398; the order 3820 /
  QC(478) claim in the introduction and Table 2 is supported by his README and NOVELTY files, not
  by that file.
