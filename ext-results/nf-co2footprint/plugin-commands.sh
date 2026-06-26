## convert all commas to \t
# sed -i 's/,/\t/g' *

# gu-cluster (memory: 0.262)
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-atacseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-atacseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-atacseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-nanoseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-nanoseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-nanoseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-chipseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-chipseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-chipseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-rnaseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-rnaseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/gu-nxf.config --tracePath traces/gu-rnaseq-3.csv --delimiter ','


# hu-cluster (memory: 0.087)
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-atacseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-atacseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-atacseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-nanoseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-nanoseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-nanoseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-chipseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-chipseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-chipseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rnaseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rnaseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rnaseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-sarek-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-sarek-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-sarek-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rangeland-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rangeland-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/hu-nxf.config --tracePath traces/hu-rangeland-3.csv --delimiter ','

# aws-cluster (0.362 / 0.343) -> 0.3525
# TDP 240W: cpu-world.com/CPUs/Xeon/Intel-Xeon%208275CL.html

nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-atacseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-atacseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-atacseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-nanoseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-nanoseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-nanoseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-chipseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-chipseq-2.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-chipseq-3.csv --delimiter ','

nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-rnaseq-1.csv --delimiter ','
nextflow plugin nf-co2footprint:postRun --config conf/aws-nxf.config --tracePath traces/aws-rnaseq-2.csv --delimiter ','
