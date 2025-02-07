#!/bin/bash

# run 1
perf stat -a -e power/energy-cores/,power/energy-pkg/,power/energy-ram/ -o perf-1.txt nextflow run nf-core/ampliseq -profile test_full,conda -c nf-conda.config --outdir out  --max_memory 16.GB > ampliseq-1.log
mv trace.csv ampliseq-1.csv
rm -rf work/ .nextflow/

# run 2
perf stat -a -e power/energy-cores/,power/energy-pkg/,power/energy-ram/ -o perf-2.txt nextflow run nf-core/ampliseq -profile test_full,conda -c nf-conda.config --outdir out --max_memory 16.GB > ampliseq-2.log
mv trace.csv ampliseq-2.csv
rm -rf work/ .nextflow/

# run 3
perf stat -a -e power/energy-cores/,power/energy-pkg/,power/energy-ram/ -o perf-3.txt nextflow run nf-core/ampliseq -profile test_full,conda -c nf-conda.config --outdir out --max_memory 16.GB > ampliseq-3.log
mv trace.csv ampliseq-3.csv
rm -rf work/ .nextflow/

# store results
mkdir ampliseq/
mv ampliseq-*.csv ampliseq/
mv perf-*.txt ampliseq/
mv ampliseq-*.log ampliseq/
