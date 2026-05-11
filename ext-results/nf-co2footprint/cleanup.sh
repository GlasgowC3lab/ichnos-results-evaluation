# cleanup commands (find and replace wf name as we go)
mv co2footprint_trace* co2fp-trace-atacseq-1.csv
mv co2footprint_report* co2fp-report-atacseq-1.html
mv co2footprint_summary* co2fp-summary-atacseq-1.txt

mv co2footprint_trace* co2fp-trace-atacseq-2.csv
mv co2footprint_report* co2fp-report-atacseq-2.html
mv co2footprint_summary* co2fp-summary-atacseq-2.txt

mv co2footprint_trace* co2fp-trace-atacseq-3.csv
mv co2footprint_report* co2fp-report-atacseq-3.html
mv co2footprint_summary* co2fp-summary-atacseq-3.txt

mv co2fp-* output/hu-cluster/

# convert tabs to commas
sed -i 's/,/\t/g' output/gu-cluster/*.csv
sed -i 's/,/\t/g' output/hu-cluster/*.csv

# convert tabs to commas
sed -i '' 's/\t/,/g' * 
