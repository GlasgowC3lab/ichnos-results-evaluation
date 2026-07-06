# cleanup commands (find and replace wf name as we go)
mv co2footprint_trace* co2fp-trace-rangeland-1.csv
mv co2footprint_report* co2fp-report-rangeland-1.html
mv co2footprint_summary* co2fp-summary-rangeland-1.txt

mv co2footprint_trace* co2fp-trace-rangeland-2.csv
mv co2footprint_report* co2fp-report-rangeland-2.html
mv co2footprint_summary* co2fp-summary-rangeland-2.txt

mv co2footprint_trace* co2fp-trace-rangeland-3.csv
mv co2footprint_report* co2fp-report-rangeland-3.html
mv co2footprint_summary* co2fp-summary-rangeland-3.txt

mv co2fp-* output/hu-cluster/

# convert tabs to commas
sed -i 's/,/\t/g' output/gu-cluster/*.csv
sed -i 's/,/\t/g' output/hu-cluster/*.csv

# convert tabs to commas
sed -i '' 's/\t/,/g' * 
