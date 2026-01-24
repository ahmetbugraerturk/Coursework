#!/usr/bin/env bash
set -euo pipefail

# Reproduce pipeline for test case 2 using directories:
#   inputs:  test2/input/{corpus2.txt,input2.txt}
#   outputs: test2/output/*

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p "$SCRIPT_DIR/output"

# 1) Compile
gcc -std=c11 -O2 -Wall -Wextra -o bpe main.c

# 2) Normalize corpus -> output/corpus2_normalized.txt
./bpe normalize "$SCRIPT_DIR/input/corpus2.txt" "$SCRIPT_DIR/output/corpus2_normalized.txt"

# 3) Learn BPE (vocab_size=100, min_freq=2)
./bpe learn "$SCRIPT_DIR/output/corpus2_normalized.txt" \
  "$SCRIPT_DIR/output/merges2.txt" "$SCRIPT_DIR/output/vocab2.txt" 100 2

# 4) Normalize the input -> output/input2_normalized.txt
./bpe normalize "$SCRIPT_DIR/input/input2.txt" "$SCRIPT_DIR/output/input2_normalized.txt"

# 5) Tokenize using learned merges -> output/tokens2.txt
./bpe tokenize "$SCRIPT_DIR/output/input2_normalized.txt" \
  "$SCRIPT_DIR/output/merges2.txt" "$SCRIPT_DIR/output/tokens2.txt"

# 6) Encode tokens to ids -> output/encoded2.txt
./bpe encode "$SCRIPT_DIR/output/vocab2.txt" \
  "$SCRIPT_DIR/output/tokens2.txt" "$SCRIPT_DIR/output/encoded2.txt"

# 7) Decode ids back to tokens -> output/decoded2.txt
./bpe decode "$SCRIPT_DIR/output/vocab2.txt" \
  "$SCRIPT_DIR/output/encoded2.txt" "$SCRIPT_DIR/output/decoded2.txt"



