# Default target
run:
	echo "Usage: make <digit>"

# If target is a single digit, compile and run
%:
	@if echo "$@" | grep -Eq '^[0-9]$$'; then \
		gcc -std=c99 -o main main.c; \
		./main test_map_$@.txt; \
	else \
		echo "Target must be a single digit (0–9)."; \
	fi
