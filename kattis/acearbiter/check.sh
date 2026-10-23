#!/bin/bash

# Usage: ./check.sh [-s]
#   -s : skip printing correct cases

# Flag
SKIP_CORRECT=false
if [[ "$1" == "-s" || "$1" == "--skip-correct" ]]; then
    SKIP_CORRECT=true
fi

# Paths
ANS_DIR="/home/zwee/codingspace/comp/misc/ans/ncpc2022-problems/acearbiter/data/secret"
BIN="runC acearbiter.c"   # wrapper to run C file

# Loop through first 20 .in files
count=0
for infile in "$ANS_DIR"/*.in; do
    # Stop after 30
    if [ $count -ge 36 ]; then
        break
    fi

    # Derive matching .ans file
    ansfile="${infile%.in}.ans"

    # Run program on input
    output=$( $BIN < "$infile" )

    # Compare with expected answer
    if diff -q <(echo "$output") "$ansfile" > /dev/null; then
        if [ "$SKIP_CORRECT" = false ]; then
            echo "🔹 Test $((count+1)): $(basename "${infile}")"
            echo "   ✅ Correct"
        fi
    else
        echo "🔹 Test $((count+1)): $(basename "${infile}")"
        echo "   ❌ Wrong Answer"
        echo "   Expected:"
        cat "$ansfile"
        echo "   Got:"
        echo "$output"
    fi

    count=$((count+1))
done
