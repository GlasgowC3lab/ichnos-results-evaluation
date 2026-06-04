#!/bin/bash

# beforehand - add_cpu_model + fix missing

experiment=$1

mkdir -p ../../temp/aflow-traces/

cp $experiment/1/trace.csv ../../temp/aflow-traces/$experiment-1.csv
cp $experiment/2/trace.csv ../../temp/aflow-traces/$experiment-2.csv
cp $experiment/3/trace.csv ../../temp/aflow-traces/$experiment-3.csv
