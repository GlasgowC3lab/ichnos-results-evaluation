## convert all commas to \t
# sed -i 's/,/\t/g' *

# gu-cluster
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-atacseq-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-atacseq-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-atacseq-3.csv

nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-nanoseq-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-nanoseq-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-nanoseq-3.csv

nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-chipseq-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-chipseq-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-chipseq-3.csv

nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-rnaseq-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-rnaseq-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-rnaseq-3.csv


# hu-cluster
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-atacseq-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-atacseq-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-atacseq-3.csv

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-nanoseq-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-nanoseq-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-nanoseq-3.csv

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-chipseq-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-chipseq-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-chipseq-3.csv

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rnaseq-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rnaseq-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rnaseq-3.csv

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-sarek-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-sarek-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-sarek-3.csv

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rangeland-1.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rangeland-2.csv
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rangeland-3.csv
