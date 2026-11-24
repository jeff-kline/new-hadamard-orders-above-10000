# Findings ledger and dispositions (24 November 2026)

Reports: [reviews/proof-audit.md](reviews/proof-audit.md) (Fable, cold proof audit),
[reviews/claims-citations-audit.md](reviews/claims-citations-audit.md) (Sonnet),
[reviews/p1-rescan-2026-11-24.md](reviews/p1-rescan-2026-11-24.md) (Sonnet). All are process-separated
AI reviews, not expert peer review.

| # | Source | Finding | Class | Disposition |
|---|---|---|---|---|
| 1 | claims | "no table extends this far" overstates (Seberry–Yamada 1992 enumeration < 40000 unread) | error | "no printed table covers them"; caveat kept in Section 4 and PRIOR-ART |
| 2 | claims | README claimed a real Gram check from entries that the release does not run | error | README and paper now describe only the exact block Gram check |
| 3 | claims | Theorem A stated without "n odd" in README, abstract, CITATION | error | added everywhere |
| 4 | claims | "Yamada–Kiyasu" used, Kiyasu never cited | gap | replaced by "Yamada's construction of order 4(q+2)" |
| 5 | claims | Lemma 1 "proved on paper" though odd r follows Glazyrin | documentation | evidence table states the dependence |
| 6 | claims | Kamali–Kharaghani also found length 19 | documentation | stated; the three used are named |
| 7 | claims | Craigen–Holzmann–Kharaghani 8(x+y) not cited | gap | cited; Theorem C new only with a dihedral pair |
| 8 | claims | process-history phrases; ATTRIBUTION placeholder | documentation | phrases removed; author confirmed the larger-fill note is Codex's |
| 9 | claims | PRIOR-ART pointed to records outside the release | gap | Codex's audit records copied to audit/golay/ |
| 10 | proof | openness.py H(4s) not an over-approximation for s ≥ 2500 | gap | made recursive; three orders still not reached; evidence repinned |
| 11 | proof | large-order checks never test that coded K* is the adjoint of K | gap | adjoint identity check added at all three orders; evidence repinned |
| 12 | proof | QH566 does not have "exactly the layout" of Lemma 2 (only Y′ does) | documentation | wording now "contains the block Y′ … exactly" |
| 13 | proof | Theorem D proof cites dihedral 15·104, 9·320; code uses complex 3·520, 18·160 | documentation | both decompositions stated |
| 14 | proof | "random unit vectors" means entries in {±1, ±i} | documentation | stated |
| 15 | proof | Lemma 1 omits zero line sums for odd r | gap | sentence added |
| 16 | proof | 824332 reasoning omitted the product routes | documentation | added |
| 17 | proof | Section 5 candidates n = 15, 21 need "not a prime power" | documentation | added |
| 18 | proof | array cited as KK Theorem 7; it is Craigen's array, KK Lemma 2 | documentation | citation corrected |
| 19 | p1 | aiXiv has no usable search | residual | logged NOT PERFORMED |
| 20 | claims | Turyn 1970 pages, Kumar repository locators, Du–Jiang corollary numbers unverified | residual | Kumar locators checked by the orchestrator (C1286.json last changed at commit 86854289, 2026-10-21; CONFERENCE.md Theorems 1 and 3 read in full); Turyn 1970 pages and Du–Jiang corollary numbers open |
