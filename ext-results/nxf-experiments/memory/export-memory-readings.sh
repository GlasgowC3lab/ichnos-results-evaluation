#!/bin/bash

filename=$1

awk -F',' '
    NR == 1 { next }
    $1 == 0  { zero_val = $4 }
    $1 >= 10 { sum += $4; count++ }
    END {
        printf "no load: %.3f W/GB | load: %.3f W/GB\n", zero_val, sum / count
    }
' "$filename"
