# Final end-to-end read of the assembled paper (commit 1dfd9d9, 24 November 2026)

Process-separated AI read; not expert peer review. Read: `paper/main.tex` (all 210 lines),
`paper/main.pdf` (pdftotext; SHA-256 matches VERIFICATION.md), `README.md`, `CITATION.cff`,
`ADMISSION.md`, `VERIFICATION.md`, plus `code/openness.py`, `evidence/openness.txt` and
`audit/golay/` where a claim pointed there. Not read: any cited source (Kumar's repository,
Glazyrin, Kamali–Kharaghani, Du–Jiang, EKLO); locators into them are unchecked by this read.

## What was checked and holds

- Arithmetic: all six factorizations; Table 1 (19882, 103042, 2803222; q = 39761, 206081,
  5606441, all prime and 1 mod 8); 206083, 2339, 1567, 2887, 1499 prime; 824331 = 3·274777,
  412165 = 5·13·17·373; 50144/92384/95936 are twice the new orders; 5(550+648) = 5990,
  16·2995 = 47920; 69232 = 16(7+4320); 94−9 = 85 and 38−9 = 29 in paper and README.
- Table 2: recomputed (Miller–Rabin) for all ten n and r ≤ 16; every listed exponent agrees.
  Source orders agree with n via 2(q+2), q = 2n−1.
- Lemma 1, r = 2: support pattern, Gram identity and line sums re-derived. Odd r: re-derived in
  full for r = 3 with a general Z (pattern, vanishing cross terms, Gram = n³I − J); the
  "W against J" separation claim re-proved for all odd r. The reduction r = 2^a r' is sound.
- Lemma 2 doubling: H Hᵀ = 2·2(q+2) I re-derived from K K* = 2(q+2) I.
- Theorem A proof: n odd gives q ≡ 1 (mod 4); n^r + 1 = (q+3)/2.
- Theorem C proof: representation relations; s g s = gᵀ on {±1, ±i, ±s} (and its failure for
  ±is, so the alphabet restriction is needed and is stated); J X J = Xᵀ; all four diagonal
  blocks and three off-diagonal blocks of the Gram matrix of the displayed array recomputed
  (they are [A,B]J+[C,D], [A,C]J−[B,D], [B,Cᵀ]+[A,Dᵀ]J and analogues); final fill step.
- Remark on 16k(m+n): dimensions and Gram identity.
- No process-history words in paper, README, CITATION, ADMISSION, VERIFICATION (grep for agent,
  Codex, Claude, pass, lane, "first comparison"; the only hit is "three passes" of pdfTeX).
- No undefined references, no overfull boxes in `paper/main.log`; cross-references resolve to
  the intended objects.

## Findings

1. **paper/main.tex:125 (and :51, code/openness.py conf_like).** "The test over-approximates
   every ingredient" is not literally true for conference matrices: the sieve treats cores as
   known at orders ≤ 4000, prime power + 1, Mathon and Seberry–Whiteman orders, but does not
   close this set under Turyn's power construction, which was known before this note (e.g.
   a symmetric conference matrix of order 45³+1 is known and is not in the set). The conclusion
   for the three orders survives, by an argument the paper gives only for 824332: the needed
   core orders are 141²+1, 321²+1, 141³+1; 141 = 3·47 and 321 = 3·107 are not sums of two
   squares, so no real symmetric base of order 142 or 322 exists, and 141³ is not a sum of two
   squares, so no symmetric conference matrix of order 141³+1 exists at all.
   Fix: (a) replace "and conference-type cores as known at every order up to $4000$ and at every
   prime power plus one" by "and conference matrices (symmetric, skew or quaternary) as known at
   every order up to $4000$, at every prime power plus one, and at the Mathon and
   Seberry--Whiteman orders"; (b) add after "None of the three orders is reached even so.":
   "Turyn powers of real symmetric conference matrices are not in this list, and need not be:
   the three core orders are $141^2+1$, $321^2+1$ and $141^3+1$, neither $141$ nor $321$ is a
   sum of two squares, so no symmetric conference matrix of order $142$ or $322$ exists, and
   $141^3$ is not a sum of two squares either." Optionally add the closure to `conf_like` and
   repin. Class: **gap**.

2. **paper/main.tex:51 (Theorem B, last sentence).** A theorem statement contains an empirical
   claim ("from ingredients known before this note") that the paper supports by a bounded test,
   not a proof. Abstract and ADMISSION scope it correctly ("the constructions listed in
   Section 4"); the theorem does not point to the test's ingredient bounds.
   Fix: end the theorem after the display and move the sentence to a remark: "\begin{remark}
   None of these orders is reached by the constructions in Table~4 of~\cite{EKLO}, or by the 2026
   families listed in Section~\ref{sec:new}, from the ingredient sets specified there.
   \end{remark}" Class: **gap** (scoping).

3. **paper/main.tex:30, README.md:32.** "a case that no product construction reaches" is an
   unscoped universal; Section 4 supports only "would need T-matrices or Williamson-type matrices
   of order 206083, which no known family supplies".
   Fix: "The odd part $206083$ of the second is a prime $p\equiv3\pmod 4$, so product
   constructions do not apply to it." Same wording in README. Class: **error** (overstatement).

4. **paper/main.tex:34.** "a matrix of order $4p$ must come from Paley's constructions, ..."
   states as necessity what is a summary of known methods.
   Fix: "the known matrices of order $4p$ come from Paley's constructions, ...". Class:
   **error** (overstatement, minor).

5. **paper/main.tex:30 and CITATION.cff:26.** "half the smallest order previously recorded for
   its odd part" omits where; Theorem D and README say "in Kumar's table".
   Fix (both): "... half the smallest order recorded for its odd part in Kumar's 2026 table."
   Class: **documentation** (scope).

6. **paper/main.tex:201 (\bibitem{Ku26}) with :40, :59, :176, :179, :186.** "Kumar's table" is
   cited as [Ku26], whose entry locates only `complex-hadamard/CONFERENCE.md` and `C1286.json`
   at commit 8685428, October 2026. The release's own records (audit/golay/family-table.md:3,
   audit/golay/AUDIT.md:15) say the table used is `FRONTIER.md` at commit d885022, a 24 November
   snapshot. The table is therefore not locatable from the bibliography, and its date is wrong.
   Fix: add to the entry "; table of least known orders: \texttt{FRONTIER.md} at commit
   \texttt{d885022}, November 2026" (confirm path and commit), or a separate \bibitem for the
   table. Class: **documentation** (credit locator).

7. **paper/main.tex:110 (Table 1 header).** "core order $n^r+1$": by the Section 2 definition
   the core has order $n^r$; $n^r+1$ is the order of the conference matrix.
   Fix: "$\QC$ order $n^r+1$". Class: **error** (label).

8. **paper/main.tex:134, :128, :148 (Table 2).** The column "$r\le16$ with $2n^r-1$ prime"
   omits $r=1$, at which $2n-1$ is prime in every row (recomputed); the text's "$r=1$ returns
   the orders of the input matrices" does not say the table omits it. The caption says Theorem A
   "applies to published quaternary conference matrices", but eight of ten rows are unextracted
   and unchecked (stated in the text only).
   Fix: header "$2\le r\le16$ with $2n^r-1$ prime"; text "the exponents $2\le r\le16$"; caption
   "Exponents $r\ge2$ for which Theorem~\ref{thm:A} applies, given the quaternary conference
   matrix of order $n+1$ (extracted and checked only for $n=141$ and $n=321$)." Class:
   **error** (table/text mismatch) and **documentation**.

9. **paper/main.tex:151.** "Theorem A does not reach any open order below $10^4$" is false for
   $r=1$ as stated (that case is Kumar's construction and did reach open orders); the argument
   also skips $n=33,35$.
   Fix: "For $r\ge2$, Theorem~\ref{thm:A} does not reach any open order below $10^4$: that would
   need $2n^2+1<2500$, so $n\le35$; among odd $n$ that are not prime powers, $2n^2-1$ is prime
   only for $n=15$ and $n=21$, which give the known orders $1804$ and $3532$ (for prime powers
   $n$, Yamada's theorem already applies)." (Checked: 2·33²−1 = 7·311, 2·35²−1 = 31·79.)
   Class: **error** (scope) and **gap**.

10. **paper/main.tex:98.** The proof of Theorem A invokes Lemma 1 for all $r\ge1$; the lemma is
    stated for $r\ge2$.
    Fix: "For $r=1$ the conference matrix is given; for $r\ge2$ Lemma~\ref{lem:power} gives a
    $\QC(n^r+1)$. In both cases $n^r+1=(q+3)/2$." Class: **gap** (trivial).

11. **paper/main.tex:76.** "the cross terms in $Z_2Z_2^*$ vanish" is inexact: the terms involving
    $Z\otimes Z$ vanish; the cross terms of $I\otimes J$ with $J\otimes I$ are the $-2J\otimes J$
    in the display. Line 80: zero line sums of $Z_2$ also use that $I\otimes J$ and $J\otimes I$
    have equal line sums $n$.
    Fix: "Since $ZJ=JZ=0$, the cross terms involving $Z\otimes Z$ vanish, the other two cross
    terms are each $-J\otimes J$, and"; and "Row and column sums of $Z_2$ are zero because those
    of $Z$ are and $I\otimes J$, $J\otimes I$ have equal line sums." Class: **gap** (wording).

12. **paper/main.tex:43, :88, :36.** "quaternary Hadamard matrix" is never defined; "quaternary
    conference matrix" is used in the abstract and introduction before its definition at :65.
    Fix: at :36 after "any quaternary conference matrix of order $(q+3)/2$" add "(zero diagonal,
    off-diagonal entries in $\{\pm1,\pm i\}$, orthogonal rows)"; at :65 add "A \emph{quaternary
    Hadamard matrix} of order $c$ is a $c\times c$ matrix $K$ with entries in $\{\pm1,\pm i\}$
    and $KK^*=cI$." Class: **documentation**.

13. **paper/main.tex:120, :176.** Undefined terms: "$\mathrm{PAF}_\alpha+\mathrm{PAF}_\beta$" and
    "Yamada's sequences" (the text before speaks of circulants $M,N$); "exponents" at :176
    (the $t$ in $2^t m$); "T-matrices", "Williamson-type matrices" in Section 4.
    Fix: (ii) "The first rows $\alpha,\beta$ of Yamada's circulants $M,N$ have periodic
    autocorrelations summing to $q\delta$ ..."; at :176 "records, for each odd part $m$, the
    least $t$ with a known Hadamard matrix of order $2^tm$; for $1567$, $2887$ and $1499$ these
    are $5$, $5$ and $6$"; one clause each for T-matrices and Williamson-type matrices or a
    pointer to \cite{SY20}. Class: **documentation**.

14. **paper/main.tex:161 with README.md:76, :90.** The paper credits the array to Craigen
    ("Craigen's Goethals--Seidel array, as stated by Kamali and Kharaghani") but cites no paper
    of Craigen; the README still says "The array is Kamali and Kharaghani's" and "the
    Kamali–Kharaghani array" (ledger item 18 corrected the paper only).
    Fix: add the Craigen reference that KK98 Lemma 2 cites (audit/golay/audit-golay.md:15 links
    a J. Combin. Math. Combin. Comput. vol. 15 paper, Theorems 9–10; verify details before
    adding); README: "The array is Craigen's form of the Goethals–Seidel array, as used by
    Kamali and Kharaghani" and "Craigen's array, the Kamali–Kharaghani seeds". Class:
    **documentation** (credit).

15. **paper/main.tex:182, :154.** "(Seberry and Yamada; Xia, Xia, Seberry and Wu)" and "the
    classical expansion of a signed-group matrix by a real Hadamard fill" name sources with no
    citation; "Craigen, Holzmann and Kharaghani~\cite{CHK02} already give order $8(m+n)$" has no
    locator although PRIOR-ART.md records Corollary 16.
    Fix: cite or replace the parenthesis by "(recorded in the release repository)"; cite Craigen
    1995 for the expansion; "\cite[Corollary~16]{CHK02}". Class: **documentation** (credit).

16. **paper/main.tex:128.** "Real symmetric conference matrices give orders that Yamada's theorem
    already reaches when $n$ is a prime power" understates and confuses: by Turyn's theorem the
    powers of a real symmetric conference matrix are real symmetric, so Yamada's theorem applies
    for every such input (inference from the statement of Turyn's theorem; not re-read here).
    Fix: "Real symmetric conference matrices give nothing new: their Turyn powers are again real
    symmetric, so Yamada's theorem already applies." Class: **style** (accuracy).

17. **paper/main.tex:102.** "contains the block $Y'$ of Lemma~\ref{lem:template}": $Y'$ is
    defined in the paragraph after the lemma, not in it. Fix: "the block $Y'$ described after
    Lemma~\ref{lem:template}". Class: **style**.

18. **paper/main.tex:125.** "(Section~\ref{sec:ai} and \texttt{audit/})": Section 7 does not
    describe the search. Fix: "(recorded in \texttt{audit/PRIOR-ART.md} of the release
    repository)". Class: **documentation**.

19. **paper/main.tex:90, :69, :80, :182.** Symbol collisions: $K_r,K_i$ (real and imaginary
    parts) beside the exponent $r$ and the unit $i$; $J$ fixed "of order $n$" at :69 but used
    at order $n^r$ (:80) and as $J_2$; $W$ is a string letter in Lemma 1 and an array in the
    remark; $q$ is a field order at :65 and $2n^r-1$ elsewhere.
    Fix: $K_{\mathrm{re}},K_{\mathrm{im}}$; at :69 "of the order required by context"; rename
    the remark's array (e.g. $G$); "a finite field of order $p'\equiv1\pmod4$". Class: **style**.

20. **paper/main.tex:120.** The parenthesis "(three each at $159052$ and $824332$, two at
    $22425772$)" follows the adjoint check, so it is unclear what is counted. Fix: move it to
    directly after "for random vectors $x$ with entries in $\{\pm1,\pm i\}$" in (iv) as
    "(three vectors each at ..., two at ...)". Class: **style**.

21. **README.md:115.** "found them at lengths 7, 9 and 15" contradicts the paper (:154: lengths
    7, 9, 15 and 19) and ledger item 6. Fix: "found them at lengths 7, 9, 15 and 19 (the first
    three are used here)". Class: **error** (README).

22. **README.md:148 vs VERIFICATION.md:19.** `make verify` is "about 2 minutes" in one and
    "about 1 minute" in the other. Fix: make them agree with the pinned run. Class:
    **documentation**.

23. **README.md:42–49.** The section "What is new" opens with a paragraph of earlier work
    (Turyn, Glazyrin, Kumar), repeated under "Earlier work". Fix: move that paragraph to
    "Earlier work" or reduce it to one clause, so the section starts with the table and the
    bullets. Class: **style**.

24. **paper/main.tex:197–198.** Bibliography order: Goethals–Seidel precedes Glazyrin. Fix: swap.
    Class: **style**.

25. **paper/main.tex:46–52.** Theorem B has no marked proof. Fix: open Section 3 with "Theorem
    \ref{thm:B} follows from Theorem~\ref{thm:A} applied to the two inputs below with the
    exponents of Table~\ref{tab:orders}; the comparison is in Section~\ref{sec:new}." Class:
    **style**.

26. **paper/main.tex:24, README.md:5–7, ADMISSION.md:36.** Draft markers ("release candidate; no
    DOI yet", "Status: draft", "an end-to-end read ... is still to be done") must be updated at
    freeze; the PDF hash in VERIFICATION.md:43 must be repinned after any edit above. Class:
    **documentation** (pre-freeze reminder).

## Not verifiable by this read (residuals, not findings)

- "every one is $4p$, $4kp$ with $k\le13$, or $8p$" (:34): the 4·odd entries in
  `code/openness.py` agree (all primes 3 mod 4, k ∈ {3,5,7,9,11,13}); the 8p entries and the
  source table were not seen.
- Locators: Kumar Theorems 1 and 3; Glazyrin Lemma 4.1 and Theorem 5; KK98 Lemmas 2, 3 and
  Theorem 7 and the alphabet {±1, ±i, ±s}; Kharaghani 1992 Lemma 7 and Theorem 9; Du–Jiang
  Corollaries 3 and 5; Turyn 1970 pages.
- The counts 94/9/85 and 38/9/29 are internally consistent; their derivation was not rerun.

## Verdict

**READY-WITH-FIXES.** No theorem or proof is wrong as written. Findings 1–3 and 6–9 should be
fixed before the freeze (one unsupported "over-approximates every ingredient", two overstated
scope sentences, one unlocatable table citation, one mislabelled table column, the r = 1
omissions in Section 5); the rest are wording, definitions and credit locators.
