# Prior-art record (P1), draft of 24 November 2026

Bounded to the sources listed. A failed or inaccessible search is recorded as such and never
counted as a negative.

## Theorems A and B (squared quaternary cores)

| Claim checked | Sources searched (24 Nov 2026) | Result |
|---|---|---|
| Orders 159052, 824332, 22425772 constructed anywhere | `gh search code` 824332, 159052, "206083 Hadamard", "39763 Hadamard", 79526, 412166 (positive control `gh search code 3356 Hadamard` hit Kumar's repository); Kumar's repository tree (3329 paths); Zaitsev's quaternary page; EKLO arXiv:2610.27175 full text; web search | not found |
| Tables covering these odd parts | EKLO ≤ 10^4; Seberry–Yamada Table A.17 and Cati–Pasechnik odd n ≤ 2999; Zaitsev quaternary list < 2000; math74 Explorer ≤ 10^4 | none covers them. Seberry–Yamada 1992 (Contemporary Design Theory) describe a computer enumeration for odd parts < 40000 (would include 39763); the printed table stops lower; the enumeration itself was not accessible |
| Construction-level check | `code/openness.py`: every EKLO Table 4 construction producing 4·odd plus 2026 families, with over-approximated ingredients | none reaches the three orders |
| Squaring / power construction for quaternary or complex conference matrices | Turyn 1971 (pp. 531–533 read; real only); Goethals–Seidel 1967 (text layer, real only); Glazyrin arXiv:2608.16116 §4 (read: Hermitian unimodular case, Lemma 4.1, Theorem 5); Et-Taoui arXiv:1409.5720 (full HTML: not found); Kharaghani–Mohammadian–Tayfeh-Rezaie–Zaitsev arXiv:2605.08661 (HTML through §4.3: not found); Kumar's NOTES/FRONTIER/CONFERENCE (not found) | KNOWN in substance (Turyn; Glazyrin for Hermitian); non-Hermitian form is a routine extension, credited as such |
| Not accessed | Delsarte–Goethals–Seidel 1971 (Canad. J. Math. 23); Craigen, Handbook ch. V.2 and JCTA 1995 on unit weighing matrices; Szöllősi's complex-conference papers; Brouwer's tables; MathSciNet; aiXiv (no usable search) | — |

## Theorems C and D (two dihedral Golay pairs)

Audit records in [golay/](golay/) (copied from the working notes, 24 Nov 2026): Kamali–Kharaghani 1998 (read), Kharaghani 1992
(Lemma 7 and Theorem 9: same order formula under an amicability hypothesis that the inputs violate),
Craigen–Holzmann–Kharaghani 2002 Corollary 16, Craigen 1995, Craigen–Kharaghani 1996/1997,
Kharaghani–Tayfeh-Rezaie 2005, Du–Jiang 2024, Seberry 2017 §4.15, the 1992, 2025 and November 2026
tables. Earlier constructions were found for the comparison orders 50144, 92384, 95936; none for
25072, 46192, 47968. Not accessed: Geramita–Seberry 1979 Appendix K, Koukouvinos 1988 thesis
Appendix II (both tabulate odd parts below 10000 by older methods).

## Pre-tag rescan (24 Nov 2026)

[reviews/p1-rescan-2026-11-24.md](reviews/p1-rescan-2026-11-24.md): GitHub code (13 queries, positive
control hit), 11 repositories cloned and grepped, arXiv listings since 2026-11-01, Zenodo, OpenAlex
cited-by of Kamali–Kharaghani 1998, Turyn 1971 and Glazyrin 2026: nothing anticipates the six orders
or either mechanism. aiXiv: NOT PERFORMED (no usable search). Repeat within 7 days of any tag.

## Signed-group check for Theorem C (24 Nov 2026)

[reviews/signed-group-check.md](reviews/signed-group-check.md): is Theorem C stated in, or an immediate
special case of, Craigen's signed-group framework? NOT FOUND. Read in full: Kamali–Kharaghani 1998
(Theorem 7 needs the second pair real), Kharaghani 1992 (Theorem 9: same formula, amicability
hypothesis fails for these inputs); partially: Craigen–Kharaghani 1996, Livinskyi's thesis restating
Craigen 1995 (Lemma 3.1 needs disjoint quasisymmetric circulants; no tensor product of remreps),
Ghaderpour–Kharaghani (Remark 3 names non-commutation as the obstacle). Craigen–Kharaghani 1997
Theorem 12 and its final example (pp. 55–58) are covered by the record [golay/audit-golay.md](golay/audit-golay.md):
Theorem 12 needs commuting, quasisymmetric or amicable inputs, and the example uses a binary second
input with a larger power of 2. Not opened in this check: Craigen 1995 original (read for the
Theorem 6 arithmetic in golay/audit-golay.md), Craigen–Holzmann–Kharaghani 2002, the Handbook chapter.
Neighbouring activity: github.com/vatskishan03/Hadamard reports dihedral pairs of length 25 (last push
2026-11-06) and uses Kamali–Kharaghani Corollary 9 only; no two-pair theorem and none of the six orders.
