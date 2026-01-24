#!/usr/bin/env bash
set -euo pipefail

# Reproduce pipeline for test case 1 using directories:
#   inputs:  test1/input/{corpus1.txt,input1.txt}
#   outputs: test1/output/*

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p "$SCRIPT_DIR/output"

# 1) Compile
gcc -std=c11 -O2 -Wall -Wextra -o bpe main.c

# 2) Normalize corpus -> output/corpus1_normalized.txt
./bpe normalize "$SCRIPT_DIR/input/corpus1.txt" "$SCRIPT_DIR/output/corpus1_normalized.txt"

# 3) Learn BPE (vocab_size=100, min_freq=2)
./bpe learn "$SCRIPT_DIR/output/corpus1_normalized.txt" \
  "$SCRIPT_DIR/output/merges1.txt" "$SCRIPT_DIR/output/vocab1.txt" 100 2

# 4) Normalize the input -> output/input1_normalized.txt
./bpe normalize "$SCRIPT_DIR/input/input1.txt" "$SCRIPT_DIR/output/input1_normalized.txt"

# 5) Tokenize using learned merges -> output/tokens1.txt
./bpe tokenize "$SCRIPT_DIR/output/input1_normalized.txt" \
  "$SCRIPT_DIR/output/merges1.txt" "$SCRIPT_DIR/output/tokens1.txt"

# 6) Encode tokens to ids -> output/encoded1.txt
./bpe encode "$SCRIPT_DIR/output/vocab1.txt" \
  "$SCRIPT_DIR/output/tokens1.txt" "$SCRIPT_DIR/output/encoded1.txt"

# 7) Decode ids back to tokens -> output/decoded1.txt
./bpe decode "$SCRIPT_DIR/output/vocab1.txt" \
  "$SCRIPT_DIR/output/encoded1.txt" "$SCRIPT_DIR/output/decoded1.txt"


