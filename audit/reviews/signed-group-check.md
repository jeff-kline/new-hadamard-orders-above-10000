# Signed-group prior-art check for Theorem C (two dihedral Golay pairs, order 16(m+n))

Date: 2026-11-24. Cold check, read-only, no computation, no subagents.

## Verdict

**(c) NOT FOUND in the sources read.** The verdict is bounded: three of the named primary sources
could not be opened this session (HTTP 403), so "not found" does not cover their full text.
The one place where a stated theorem could still contain the claim is
Craigen–Kharaghani 1997, Theorem 12 and the closing block example (pp. 55–58), followed by the
original text of Craigen 1995.

The priority question (do 25072, 46192, 47968 already follow from published inputs?) is therefore
answered "no route found", not "no route exists".

## What was read

| Source | Access | Extent |
|---|---|---|
| Kamali–Kharaghani 1998, AJC 18, 139–145 | AJC OCR PDF | In full |
| Kharaghani 1992, AJC 6, 293–303 | AJC OCR PDF | In full (OCR drops condition (i) of the block Golay definition) |
| Craigen–Kharaghani 1996, AJC 13, 89–... ("A combined approach") | AJC OCR PDF | All theorem statements scanned; §4 (seed matrices, Thms 13–19) read |
| Craigen 1995, JCTA 71, 241–254 | academia.edu 403, ScienceDirect 403, no CORE or Wayback copy | **Not read at source.** Read only through Livinskyi's restatement (below) |
| Livinskyi, MSc thesis, Manitoba (handle 1993/8915), supervised by Craigen | mspace PDF | Ch. 2–3 read in full: Thm 2.2, Cor 2.3–2.4, Lemma 3.1, Thm 3.7, Cor 3.8–3.9, Thm 3.10–3.11 (those marked [C1] restate Craigen 1995) |
| Craigen–Kharaghani 1997, DCC 12, 49–58 | academia.edu 403, Springer paywall, Semantic Scholar "CLOSED" | **Not read** |
| Craigen–Holzmann–Kharaghani 2002, Discrete Math. 252 | ScienceDirect 403 | **Not read** |
| Craigen, Handbook chapter | — | **Not read** |
| Ghaderpour–Kharaghani, arXiv 1502.07668 | arXiv | Theorem list scanned; Lemma 4, Theorem 5, Remark 3 read |
| Ghaderpour, arXiv 1709.02806 | arXiv | §1–2 read (definitions of signed group, remrep, SH) |
| Du–Jiang arXiv 2401.15381; Ghaderpour–Kharaghani arXiv 1003.4001; Egan, "Phased unitary Golay pairs" (DCU preprint) | arXiv / DCU | Keyword scan only (dihedral, remrep, signed group, tensor) |
| GitHub: `gh search repos` / `gh search code` for "dihedral Golay", "signed group Hadamard" | — | One relevant repository, see below |
| Web search: "dihedral Golay" with "signed group", "tensor", "16(m+n)", "two dihedral Golay" | — | No hit beyond Kamali–Kharaghani 1998 |

Earlier notes in `audit/golay/audit-golay.md` summarise Craigen 1995 Theorems 5–6 and
Craigen–Kharaghani 1997 Corollary 10 and Theorem 12. I did not treat them as independent evidence;
they are the only record here of those texts and I could not re-read the originals against them.

## Findings (verified in the text read)

1. **Kamali–Kharaghani 1998.** Theorem 7 (p. 143) requires "a, b a DGS of length m free of ±is
   entries and c, d a GS of length n", the second pair real. Corollaries 8–9 give 4(g₁g+g₂)
   dihedral and 8(g₁g+g₂) real, g ∈ {7, 9, 15}. The remark after Corollary 5 (p. 143) reads:
   "Similarities with complex Golay sequences do not carry over to include the product of lengths
   of two DGSs. Generally, condition (i) of the definition is hard to achieve." No statement
   combines two dihedral pairs, or a dihedral pair with a complex pair, by sum of lengths.
   Lemma 2 as printed takes circulants "with all entries in {±1, ±i}"; Theorem 7 applies the array
   to D-entries through Lemma 6.

2. **Kharaghani 1992.** Lemma 7 and Theorem 9 (p. 298): block Golay sequences of lengths n, m and
   block size k with "FGᵗ = GFᵗ for all entries G, F of A, B, E, D" give a Hadamard matrix of order
   4(n+m)k. With k = 4 this is the same order formula 16(m+n). The amicability hypothesis fails for
   the present inputs: with F = H₄ and G = (i⊗I₂)H₄, FGᵗ = −4(i⊗I₂) and GFᵗ = +4(i⊗I₂). Right
   multiplication by any fixed matrix does not change FGᵗ, so no uniform dense fill repairs this.
   Not a special case.

3. **Craigen–Kharaghani 1996.** Theorems 13 and 19–20 use (N,k)-seed matrices (a Hadamard matrix
   amicable to an orthogonal set) with disjoint complementary (0,±1) pairs. Theorem 19 does tensor
   two seed systems (L = H⊗K, F = Qᵢ⊗Rⱼ), and p. 99 notes that seed matrices give block Golay
   sequences (lengths 3, 5 at block size 4; 15 at block size 2⁴). The tensor idea is present for
   real amicable seeds, not for dihedral or complex Golay coefficients, and the resulting orders
   have the shape 4N(w+k+1), 4N(kv+1).

4. **Craigen 1995, via Livinskyi.** Cor 2.3: SH(n; S) with a remrep of degree m, m a Hadamard order,
   gives H(mn). Lemma 3.1 [C1] needs A, B "normal, commuting, disjoint, quasisymmetric (0,S)-matrices"
   and doubles the remrep degree. Theorem 3.10 [C1]: t binary pairs of total length L give order
   4^{t+1}(2L+1); Theorem 3.11: complex pairs give 2^{2t+3}(2L+1). The restated chapters contain no
   product of signed groups with tensor remrep and no formula 4·deg·(m+n). *Inference:* Lemma 3.1
   cannot yield 16(m+n), because it needs disjoint quasisymmetric circulants, which forces the
   zero-padded period 4L+2 and one remrep doubling per sequence; two pairs give at least 64(2L+1).

5. **Ghaderpour–Kharaghani 2015, Remark 3:** "if the signed group is not abelian, the circulant
   matrices that obtain from Lemma 4 do not necessarily commute, and Theorem 5 may fail." The
   non-commutation obstacle is named and left unresolved there; no tensor-factor remedy is given.
   This is indirect evidence that the device is not standard in this line.

6. **GitHub.** `vatskishan03/Hadamard` (public, created 2026-10-11, last push 2026-11-06, commit
   d885022144) has `search/dcs/` and NOTES §104 on dihedral Golay sequences. It uses only
   Kamali–Kharaghani Corollary 9 (orders 6712, 8248, 14344), states "Its only lever is Lemma 3
   (DCS × Golay)", and reports DCS of length 25 from an ansatz search. Code search in that
   repository for 25072 returned nothing; hits for 46192 and 47968 are unrelated numeric data.
   No two-pair theorem. It is an active neighbour working on the same objects.

## Assessment of distance (inference)

The claim is not stated in what I read, and no stated theorem I read has it as a special case.
The proof is close to Kamali–Kharaghani Theorem 7: the same four concatenations and the same
Craigen–Goethals–Seidel array, with coefficient ring D⊗D in place of D and reflector R⊗s⊗s.
The step that is not in the sources read is placing the two pairs on commuting tensor factors so
that the second pair need not be real. A referee familiar with Craigen–Kharaghani 1997 could still
regard it as a corollary of their Theorem 12 if that theorem's hypotheses are abstract enough
(two signed-group matrices that commute, with a quasisymmetry or amicability condition). That is
the specific check left open.

## The three orders

- 25072 = 16(7+1560), 46192 = 16(7+2880): length 7 is dihedral and not complex Golay
  (Kamali–Kharaghani, p. 141); 1560 and 2880 are divisible by 3, so they are not real Golay lengths.
  Theorem 7 of Kamali–Kharaghani does not apply to these pairs.
- 47968 = 16(182+2816): 2816 = 2⁸·11 is not a real Golay length; 182 = 2·7·13 is not of the known
  complex Golay form 2^{a+u}3^b5^c11^d13^e.
- Hand arithmetic, not machine-checked: 25072 = 8·3134, and 3134 = g·g₁+g₂ has no solution with
  g ∈ {7, 9, 15} and g₁, g₂ real Golay numbers, so Corollary 9 does not reach 25072. I did not
  repeat this for 46192 and 47968, nor re-run the complex-pair test 8(m+n); the repository's
  `audit/golay/AUDIT.md` records both as negative.

## To close the gap

Obtain and read at source: Craigen–Kharaghani 1997 §4, Theorem 12, Corollary 10 and the final
example; Craigen 1995 pp. 244–249 (signed-group products, Theorems 5–6); Craigen–Holzmann–Kharaghani
2002 Theorems 10, 15, Corollary 16. All three were blocked to automated fetch; a browser download
by the author would settle it.
