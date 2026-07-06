#!/bin/bash

for num in {1..2}
do
    python format-trace.py rangeland/Run$num/task_data rangeland-$num
    python format-trace.py sarek/Full_$num/task_data sarek-$num
done
