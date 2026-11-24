SHELL := /bin/sh
PY ?= python3

PDFLATEX ?= pdflatex
export SOURCE_DATE_EPOCH := 1795478400
export FORCE_SOURCE_DATE := 1
export OPENBLAS_NUM_THREADS := 1
export OMP_NUM_THREADS := 1
export VECLIB_MAXIMUM_THREADS := 1
export MKL_NUM_THREADS := 1

QH566_URL := https://www.cs.uleth.ca/~zaitsevv/matrices/QH566.txt
QH566_SHA := 4fbdcd2f44c7d654c2328992a44fbeafac6783ad91862137169d1c732da64355

.PHONY: paper fetch verify verify-big

# Three passes from a clean extraction; no inherited auxiliaries are required.
paper:
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	@! grep -E 'Warning:|Overfull|undefined references|undefined citations' paper/main.log
	@echo "paper built: paper/main.pdf"

# Zaitsev's matrix has no stated license, so it is downloaded rather than redistributed.
fetch:
	@test -f inputs/QH566.txt || curl -sSfL -o inputs/QH566.txt $(QH566_URL)
	@echo "$(QH566_SHA)  inputs/QH566.txt" | shasum -a 256 -c -

# Theorems A and B: controls, orders 159052 and 824332, openness sieve; Theorem D: entry-level
# exact Gram checks at 25072, 46192, 47968 (about two minutes in total on one core; NumPy needed
# for the first part, the second uses only the standard library). Compares with evidence/.
verify: fetch
	@mkdir -p build
	@$(PY) code/verify_orders.py > build/orders.txt
	@$(PY) code/openness.py 159052 824332 22425772 2572 5788 9172 2396 9356 > build/openness.txt
	@cd code/golay && $(PY) mixed_entry.py --check > ../../build/golay.txt
	@for f in orders.txt openness.txt golay.txt; do \
	  if cmp -s evidence/$$f build/$$f; then echo "MATCH $$f"; else echo "MISMATCH $$f"; exit 1; fi; done
	@echo "verify: all outputs match evidence/"

# Order 22425772 (r = 3): about five minutes and 2 GB on one core.
verify-big: fetch
	@mkdir -p build
	@$(PY) code/verify_orders.py --big > build/orders-big.txt
	@if cmp -s evidence/orders-big.txt build/orders-big.txt; then echo "MATCH orders-big.txt"; \
	  else echo "MISMATCH orders-big.txt"; exit 1; fi
