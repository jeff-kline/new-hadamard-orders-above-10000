# Claims-consistency and citation audit (read-only), 24 Nov 2026

Scope: README.md, paper/main.tex, CITATION.cff, ADMISSION.md, audit/PRIOR-ART.md, audit/ATTRIBUTION.md. No computation was run. Arithmetic spot-checks were by hand. Standard fetched: the research-program page (claims no stronger than the proof; abstract, README and paper describe the same result; novelty labelled, with limits of the search stated).

Classes: error / gap / documentation. "main.tex:N" are line numbers of paper/main.tex.

## Verified consistent (no action)

- All six orders and their factorizations match everywhere: 159052 = 4(2*141^2+1), 824332 = 4(2*321^2+1), 22425772 = 4(2*141^3+1), 25072 = 16*1567, 46192 = 16*2887, 47968 = 32*1499 = 16*2998.
- Table 1 arithmetic (core orders, q, odd parts, the factorizations of 39763 and 5606443), and the Theorem D length decompositions (7+1560, 7+2880, 182+2816), all check.
- The Section 5 table's n values match the quoted Zaitsev/Kumar orders via n = (q+3)/2 - 1.
- The counts 94 / nine / 85 and 38 / nine / 29 are mutually consistent between README:72-75 and main.tex:179 and the Remark that follows it.
- Lemma 1 (r = 2) was re-derived by hand and is correct.
- Section numbering in README matches the paper (Section 4 = newness, Section 5 = table).

## Findings

1. **README.md:31; main.tex:30 (abstract); main.tex:122-123; PRIOR-ART.md:11.** The claim is "No published table of known Hadamard orders extends this far", under the section title "Why the orders of Theorem B are new". main.tex:123 and PRIOR-ART:11 concede that Seberry–Yamada 1992 describe a computer enumeration for odd parts below 40000, which "would include 39763", i.e. order 159052. The enumeration was never accessed. So novelty of 159052 specifically is not established, and the abstract and README do not say so. Fix: weaken the abstract and README to "no table we could access"; retitle Section 4 to "Why the orders of Theorem B appear to be new" (or "What we checked"); label 159052 "apparently new; Seberry–Yamada 1992 enumeration for odd parts < 40000 not accessible". Add the same caveat to the ADMISSION claim 2 and to the README Evidence row. Class: error (overstatement).

2. **README.md:126 vs main.tex:179.** The README Evidence row says "full real Gram check from the entries". The paper says that this second independent check "was run during this work but is not among the release's verification targets". The README row and Reproduce table (README:137) imply it is part of the release. Fix: state in the README that the full real Gram check is not reproduced by `make verify` (or add it to the target), and drop "during this work" (see item 14). Class: error.

3. **main.tex:30, 36 (and README:27, CITATION.cff:19): "Yamada–Kiyasu".** Kiyasu is never cited, and no source is given for what the Yamada–Kiyasu construction is. Kumar's repo uses the label, but the paper and README present it as established. Fix: add a bibitem (Kiyasu–Zukeda or whichever source Kumar cites) or write "Yamada's construction, in the form used in [Ku26]". Class: gap.

4. **Theorem A statement omits "n odd" in README intro:21-24, main.tex:30 (abstract), CITATION.cff:15-17.** README "What is new" (:56-58), ADMISSION:16 and Theorem A (main.tex:42) include "n odd". Without it, the intro/abstract statement is stronger than the theorem (q = 2n^r - 1 ≡ 1 mod 4 needs n odd). The README intro also lacks the "prime q ≡ 1 mod 4" consequence. Fix: add "n odd" in the abstract, README intro and CITATION. Class: error (statement mismatch).

5. **Theorem A scope: paper vs README/ADMISSION.** The paper's Theorem A also yields a quaternary Hadamard matrix of order 2(q+2). README and ADMISSION state only the real 4(q+2). Fix: either mirror the paper or say "(and a quaternary Hadamard matrix of order 2(q+2))". Class: documentation.

6. **Symbols and terms used before definition.**
   - main.tex abstract and intro (:30, :33-:46): "quaternary conference matrix", "quaternary Hadamard matrix", "dihedral Golay pair" and Theorem A–D use these terms before Section 2/6 define them. The README defines "quaternary conference matrix" but not "quaternary Hadamard matrix".
   - "Q^*" and "J^2 = nJ" (main.tex:64-70) are used without defining the adjoint.
   - "PAF_α, PAF_β" and "Yamada's sequences" appear at main.tex:120 without definition.
   - README:16-24 uses "Turyn's power construction" before saying what it does.
   - main.tex:155 defines a dihedral Golay pair as having "complementary aperiodic autocorrelations" without defining that autocorrelation for non-commuting entries.
   Fix: add a one-sentence definition on first use (conjugate transpose; "quaternary" = entries in {±1, ±i}; PAF as periodic autocorrelation function). Class: gap.

7. **main.tex:80 (Lemma 1 proof, r ≥ 3) vs README:119 "proved on paper".** The odd r ≥ 3 case is delegated to Glazyrin: "Glazyrin's proof shows ... his cancellation argument then gives Z_rZ_r^* = n^r I - J". Glazyrin's setting (checked via arXiv HTML) is cores of ETFs, i.e. Hermitian, using W^2 where this paper uses WW^*. The substitution is asserted, not shown. README:61 does say "the proof is Turyn's and Glazyrin's with one substitution", which is honest. Fix: either write out the cancellation for WW^* or relabel the Evidence row "proved for r = 2; r ≥ 3 by adaptation of [Gl26, Theorem 5], checked exactly on orders 5 (r = 3, 5) and 13 (r = 3)". Class: gap.

8. **main.tex:120: "Exactness of (ii)–(v) relies on rounding..."** Items (iii) and (iv) are randomized, so "exactness" of (ii)–(v) is a misnomer. The claim "a wrong entry ... fails with probability at least 1/2 per vector" is stated without the distribution or an argument. Fix: say "(ii) and the input checks are exact up to FFT rounding; (iii)–(iv) are randomized"; justify or soften the 1/2 bound. Class: gap.

9. **main.tex:125: "(Section~\ref{sec:ai} and audit/)".** Section 7 (Role of AI) says nothing about the GitHub/Zenodo/arXiv searches, so the cross-reference does not lead to the search record. Also "the release repository records the sources, the reviews and their dispositions" (README:149-150, main.tex:190) is not true of the tree as it stands: audit/ contains PRIOR-ART.md and ATTRIBUTION.md (plus this report), and PRIOR-ART:18 points to `reviews/multi-order-2026-11-24/`, which is not in the release. Fix: point to audit/PRIOR-ART.md; ship or drop the reviews directory (or mark the citation as external). Class: gap.

10. **Process-history phrases in reader-facing prose.**
    - main.tex:179: "that a first comparison did not find elsewhere; a later check found" and "was run during this work".
    - README and main.tex otherwise clean. The grep for agent/lane/Codex/Claude/pass was clean except as below.
    - PRIOR-ART.md:18: "Codex's audit records in reviews/multi-order-2026-11-24/".
    - ATTRIBUTION.md:11-13 names "Claude (Anthropic)" and "Codex (OpenAI)" and carries the placeholder "[author to confirm which system]" at :13.
    Fix: rewrite main.tex:179 as "A comparison with earlier constructions found nine of the 94 earlier; priority is unresolved for the other 85"; resolve the ATTRIBUTION:13 placeholder; give vendor-neutral phrasing in PRIOR-ART:18 (or keep vendor names only in ATTRIBUTION). Class: documentation.

11. **Sentences about earlier work that omit what the work achieved.**
    - README:107-109 "Du and Jiang ... certified many complex Golay lengths" is vague; the paper's own remark (main.tex Remark on 47920) uses their Corollaries 3 and 5 for a four-phase complementary quadruple, which is different. State what DJ proved (arXiv title: Golay complementary sequences of arbitrary length and asymptotic existence of Hadamard matrices).
    - README:107: "Craigen, Holzmann and Kharaghani (2002) gave 8(x+y) for complex Golay pairs" has no bibitem in the paper, and x, y are undefined. EKLO Table 4 lists "Craigen–Holzmann–Kharaghani: 8(x+y)" (1001 orders). The complex-pair case of Theorem C (16(m+n)) then needs a sentence on its relation to CHK 8(x+y): is the complex special case new, or only the dihedral case? README:65-68 and main.tex:40 say "any two such pairs, or complex Golay pairs, can be combined", which reads as a novelty claim for the complex case.
    - main.tex:123 lists "Agaian, Craigen–Seberry–Zhang, Craigen–Holzmann–Kharaghani, Cooper–Wallis, Spence, Mathon, Seberry–Whiteman" without citations or results. They are cited only by implication via EKLO. Fix: cite EKLO Table 4 explicitly for the list, or add bibitems.
    Class: gap.

12. **Theorem D novelty label.** README:69-71 ("Kumar's table records only twice these sizes"), ADMISSION:23-25 and CITATION say "each half the smallest order previously recorded", without "in Kumar's table" in the paper abstract (main.tex:30) and CITATION. The abstract thus reads as a claim about all prior literature. PRIOR-ART:21-24 found earlier constructions of the comparison orders in other sources but none for the three orders, which supports "apparently new", but it is never written that way. Also "only" at README:70 is imprecise (the word suggests a defect in the table). Fix: "each half the smallest order recorded in Kumar's 2026 table for its odd part; apparently new, within the sources searched". Class: gap.

13. **KK98 content (main.tex:154; README:104).** "Kamali and Kharaghani found such pairs of lengths 7, 9 and 15" omits length 19: the KK98 abstract says "lengths 7, 9, 15, and 19" (the length-19 pair has ±is entries, so it is excluded from their Theorem 7). Verified from the PDF at ajc.maths.uq.edu.au/pdf/18/ocr-ajc-v18-p139.pdf. Fix: "lengths 7, 9, 15 and 19 (only 7, 9, 15 free of ±is entries, as their Theorem 7 requires)". Also say whether the length-19 seed is usable in Theorem C (the "over all published inputs" count at main.tex:179 depends on it). Class: gap.

14. **main.tex:179 and :190+ (counts) vs the Section 5 claim "Theorem A applies to every known QC" (main.tex:127).** The Section 5 table covers 10 values of n, but Zaitsev's page lists more quaternary orders (e.g. QH142, QH322, QH238 ... through 1966). The selection criterion (only orders 2(q+2) with q prime ≡ 1 mod 4?) is not stated. Fix: say "for the Zaitsev/Kumar orders of the form 2(q+2) with q prime". Class: gap. (Inference: the table's rows are consistent with that rule; I did not verify that no other Zaitsev order fits it.)

15. **main.tex:151: "Theorem A does not reach any open order below 10^4 ... n ≤ 35".** The bound n ≤ 35 holds for r ≥ 2 only; for r = 1 Theorem A is Kumar's, and r ≥ 3 needs n ≤ 10. It is correct as a bound but the sentence should say "for r ≥ 2". Class: documentation.

16. **main.tex:102: "its upper left 141×141 corner minus I".** The corner is of the block Y' (rows 2–283, columns 285–566), not of K. As written it reads as the corner of K. Fix: "the upper left 141×141 corner of Y', minus I". Class: documentation.

17. **EKLO locator (main.tex:123 "family 4(4q²+3) of [EKLO, Theorem 7]"; README:53).** EKLO's Theorem 7 is a general abelian-group construction; the family 4(4q²+3) is named in their Section 4 as an instance (G = Z_2² × F_{q²}, S = F_{q²}, k = 4). Fix: "the family 4(4q²+3) obtained from [EKLO, Theorem 7]". Class: documentation. Also: EKLO v2 (3 Nov 2026) abstract says 85 open orders ≤ 10^4 (10 closed since v1); its text still says 95. The release cites v2 but states no count, so there is no mismatch; the count 85 in the release (unresolved orders) is unrelated and could be confused with it (README:73 and main.tex:179). Consider writing "85 unresolved orders of this family" to avoid the coincidence.

18. **Placeholders and status text.** ATTRIBUTION.md:13 "[author to confirm which system]" is unresolved. The README Status line (README:5-7) correctly says draft; ADMISSION gates P1, A1, R1 are all open, consistent with the draft state.

19. **CITATION.cff.** The abstract (CITATION:12-27) says "no construction checked by the author", while the paper says "we", fine. It lists only three references (Turyn: no pages; Kamali–Kharaghani: given name "F." only; Kumar: "K."). Class: documentation, optional.

20. **Terminology.** README and ADMISSION mix "size" and "order" (README:14-16 vs paper "order"). Class: documentation.

## Citations (B)

Verified against authoritative sources:

| Bibitem | Result |
|---|---|
| Tu71 Turyn, On C-matrices of arbitrary powers, Canad. J. Math. 23 (1971) 531–535 | Confirmed (Crossref). |
| GS67 Goethals–Seidel, Orthogonal matrices with zero diagonal, Canad. J. Math. 19 (1967) 1001–1010 | Confirmed (Crossref). |
| Ya89 Yamada, Some new series of Hadamard matrices, J. Austral. Math. Soc. Ser. A 46 (1989) 371–383 | Confirmed (Crossref). |
| Mi91 Miyamoto, A construction of Hadamard matrices, JCTA 57 (1991) 86–108 | Confirmed (Crossref, author Masahiko). |
| KK98 Kamali–Kharaghani, Dihedral Golay sequences, Australas. J. Combin. 18 (1998) 139–145 | Confirmed (journal PDF title page). Lemma 3 (DGS × binary GS, length nm) and Theorem 7 (order 4(m+n) array, a, b DGS free of ±is, c, d GS) read in the scanned PDF and match how the paper uses them. See item 13 for length 19. |
| Kh92 Kharaghani, Block Golay sequences with applications, Australas. J. Combin. 6 (1992) 293–303 | Confirmed (PDF title page). Lemma 7 (hypothesis: all entries of A, B, E, D pairwise amicable, FG^t = GF^t) and Theorem 9 (order 4(n+m)k) read in the PDF and match the paper's description. |
| SY92 Seberry–Yamada, in Dinitz–Stinson (eds.), Contemporary Design Theory, Wiley 1992, 431–560 | Confirmed by the reference list of KK98 (same editors, publisher, pages). The enumeration to 40000 is not verified (item 1). |
| SY20 Seberry–Yamada, Hadamard Matrices, Wiley 2020 | Confirmed (Crossref, Wiley, 2020). The bibitem title "Hadamard Matrices: Constructions using Number Theory and Linear Algebra" is the subtitle as I recall it; Crossref shows only "Hadamard Matrices". |
| Gl26 Glazyrin, arXiv:2608.16116 | Title and sole author (Alexey Glazyrin) confirmed; v1 17 Aug 2026. Lemma 4.1 and Theorem 5 exist as cited and say what the release says (zero-diagonal Hermitian unimodular cores; W_2 = W⊗W + I⊗J − J⊗I; Theorem 5 for all r ≥ 2). Remark: his statements are for ETF cores, parameter m. |
| DJ24 Du–Jiang, arXiv:2401.15381 | Title and authors (Cheng Du, Yi Jiang) confirmed; submitted 27 Jan 2024. Corollaries 3 and 5 were not reached (PDF/HTML not read). |
| CP24 Cati–Pasechnik, arXiv:2411.18897 | Authors Matteo Cati and Dmitrii V. Pasechnik; title confirmed; v2 30 Aug 2025 (so "2025" for v2 is right). The abstract page says the paper was withdrawn from Special Matrices. Initials in the bibitem are correct. |
| EKLO Egan–Kotsireas–London–Ó Catháin, arXiv:2610.27175 | Title and authors confirmed; v2 3 Nov 2026. Table 4 confirmed (it includes Spence, Mathon, Seberry–Whiteman, Cooper–Wallis, Paley/Miyamoto blocks, Williamson, Miyamoto I–III, Yamada q ≡ 5 and 1 mod 8, CHK 8(x+y), etc.). Open-order shapes 4p, 4kp (k ≤ 13), 8p confirmed. |

Not verifiable in this session:
- Tu70 Turyn, Complex Hadamard matrices, Combinatorial Structures and their Applications (1970) 435–437: no authoritative hit in the search available. Please confirm against MathSciNet or zbMATH.
- Ku26 Kumar, github.com/vatskishan03/Hadamard: repo exists, Apache-2.0, README title "New Hadamard matrices", mentions the Yamada–Kiyasu template (q = 641). Not confirmed from the repo front page: `complex-hadamard/CONFERENCE.md`, `C1286.json`, commit 8685428, "Theorem 3" (main.tex:87) and "Theorem 1" (main.tex:102). These locators need a check against the commit.
- Za26 Zaitsev, www.cs.uleth.ca/~zaitsevv/quaternary.html: QH470 and QH566 are listed, and the page says the matrices were "found via unpublished approaches", so the README:101 wording is accurate.
- KK98 Corollary 9 / CHK 2002 Corollary 16 / Du–Jiang corollaries: not reached.
- Crossref returned HTTP 429 on some queries; the CHK 2002 entry (Discrete Math. 252 (2002) 73–89, "Complex Golay sequences: structure and applications") is confirmed by a later Crossref hit but is not cited in the paper (see item 11).

Hedges: the claims about Miyamoto's theorem (4p from p−1 for p ≡ 1 mod 4) at main.tex:33, Belevitch r = 2 in GS67 (main.tex:Remark after Lemma 1), and EKLO positive control 9172 were not verified here.
