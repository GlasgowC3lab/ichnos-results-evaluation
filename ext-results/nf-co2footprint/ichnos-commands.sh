#!/bin/bash

# hu - schedutil (mem draw, mem GB, no. nodes = 4) 
python3 -m src.scripts.IchnosCF hu-chipseq-1 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-chipseq-2 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-chipseq-3 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-rnaseq-1 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-rnaseq-2 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-rnaseq-3 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-rangeland-1 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-rangeland-2 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-rangeland-3 de-2025-11-17-2025-11-24 schedutil_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-sarek-1 de-2026-02-07-2026-02-09 schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-sarek-2 de-2026-02-07-2026-02-09 schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-sarek-3 de-2026-02-07-2026-02-09 schedutil_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-nanoseq-1 de-2026-03-05-2026-03-07 performance_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-nanoseq-2 de-2026-03-05-2026-03-07 performance_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-nanoseq-3 de-2026-03-05-2026-03-07 performance_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-atacseq-1 de-2026-02-20-2026-02-24 performance_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-atacseq-2 de-2026-02-20-2026-02-24 performance_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-atacseq-3 de-2026-02-20-2026-02-24 performance_linear 5 1.0 0.392 256 4


# gu - ondemand (mem draw, mem GB, no. nodes = 4)
python3 -m src.scripts.IchnosCF gu-chipseq-1 gb-2026-01-28-2026-01-30 ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-chipseq-2 gb-2026-01-28-2026-01-30 ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-chipseq-3 gb-2026-01-28-2026-01-30 ondemand_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-rnaseq-1 gb-2026-01-28-2026-01-30 ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-rnaseq-2 gb-2026-01-28-2026-01-30 ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-rnaseq-3 gb-2026-01-28-2026-01-30 ondemand_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-nanoseq-1 gb-2026-02-10-2026-02-12 ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-nanoseq-2 gb-2026-02-10-2026-02-12 ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-nanoseq-3 gb-2026-02-10-2026-02-12 ondemand_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-atacseq-1 gb-2026-02-27-2026-02-28 ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-atacseq-2 gb-2026-02-27-2026-02-28 ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-atacseq-3 gb-2026-02-27-2026-02-28 ondemand_linear 5 1.0 0.392 64 4



# use marginal carbon intensity

# hu - schedutil (mem draw, mem GB, no. nodes = 4) 
python3 -m src.scripts.IchnosCF hu-chipseq-1 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-chipseq-2 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-chipseq-3 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-rnaseq-1 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-rnaseq-2 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-rnaseq-3 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-rangeland-1 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-rangeland-2 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-rangeland-3 de-17112025-24112025-marg schedutil_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-sarek-1 de-07022026-09022026-marg schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-sarek-2 de-07022026-09022026-marg schedutil_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-sarek-3 de-07022026-09022026-marg schedutil_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-nanoseq-1 de-05032026-07032026-marg performance_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-nanoseq-2 de-05032026-07032026-marg performance_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-nanoseq-3 de-05032026-07032026-marg performance_linear 5 1.0 0.392 256 4

python3 -m src.scripts.IchnosCF hu-atacseq-1 de-20022026-24022026-marg performance_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-atacseq-2 de-20022026-24022026-marg performance_linear 5 1.0 0.392 256 4
python3 -m src.scripts.IchnosCF hu-atacseq-3 de-20022026-24022026-marg performance_linear 5 1.0 0.392 256 4


# gu - ondemand (mem draw, mem GB, no. nodes = 4)
python3 -m src.scripts.IchnosCF gu-chipseq-1 gb-28012026-30012026-marg ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-chipseq-2 gb-28012026-30012026-marg ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-chipseq-3 gb-28012026-30012026-marg ondemand_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-rnaseq-1 gb-28012026-30012026-marg ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-rnaseq-2 gb-28012026-30012026-marg ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-rnaseq-3 gb-28012026-30012026-marg ondemand_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-nanoseq-1 gb-10022026-12022026-marg ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-nanoseq-2 gb-10022026-12022026-marg ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-nanoseq-3 gb-10022026-12022026-marg ondemand_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-atacseq-1 gb-27022026-28022026-marg ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-atacseq-2 gb-27022026-28022026-marg ondemand_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-atacseq-3 gb-27022026-28022026-marg ondemand_linear 5 1.0 0.392 64 4


# background models experiment
# gu - ondemand (mem draw, mem GB, no. nodes = 4)
python3 -m src.scripts.IchnosCF gu-chipseq-1 gb-2026-01-28-2026-01-30 ondemand-bg_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-chipseq-2 gb-2026-01-28-2026-01-30 ondemand-bg_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-chipseq-3 gb-2026-01-28-2026-01-30 ondemand-bg_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-rnaseq-1 gb-2026-01-28-2026-01-30 ondemand-bg_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-rnaseq-2 gb-2026-01-28-2026-01-30 ondemand-bg_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-rnaseq-3 gb-2026-01-28-2026-01-30 ondemand-bg_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-nanoseq-1 gb-2026-02-10-2026-02-12 ondemand-bg_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-nanoseq-2 gb-2026-02-10-2026-02-12 ondemand-bg_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-nanoseq-3 gb-2026-02-10-2026-02-12 ondemand-bg_linear 5 1.0 0.392 64 4

python3 -m src.scripts.IchnosCF gu-atacseq-1 gb-2026-02-27-2026-02-28 ondemand-bg_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-atacseq-2 gb-2026-02-27-2026-02-28 ondemand-bg_linear 5 1.0 0.392 64 4
python3 -m src.scripts.IchnosCF gu-atacseq-3 gb-2026-02-27-2026-02-28 ondemand-bg_linear 5 1.0 0.392 64 4
