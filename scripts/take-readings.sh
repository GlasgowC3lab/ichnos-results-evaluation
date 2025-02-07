#!/bin/bash

## clone turbostress and cd into dir
# git clone https://github.com/teads/turbostress.git
# cd turbostress
# go build cmd/main.go
# chown +x main

## setup and adjust for governor and min + max frequency

mkdir output

## generate ts reports for ondemand governor
sudo ./main --load-step 10 | tee ts-gov-1.csv
sudo ./main --load-step 10 | tee ts-gov-2.csv
sudo ./main --load-step 10 | tee ts-gov-3.csv

for source_file in ts-gov-1.csv ts-gov-2.csv ts-gov-3.csv
do
  tail -n 15 ./$source_file >> ./output/$source_file
done
