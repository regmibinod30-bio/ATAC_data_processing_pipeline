Updated ATAC-seq analysis pipeline

## Overview
This repository contains the scripts and outputs of ATAC-seq pipeline.

## Repository map:
### script/
This directory contains `hg38_Snakefile` and `mm10_Snakefile` and associated
scripts.

### `hs_output`/
This directory contains the outputs of `hg38_Snakefile` script.

### `mm_output`/
This directory contains the outputs of `mm10_Snakefile` script.

## Major changes from existing pipeline:
Followings are the highlights of the updated pipeline:
 - The script is implemented in the newest version of snakemake software (v6.8.2).
 - All the tools are updated with the newest version except bowtie and python.
 - fastQC is integrated with rule trim.
 - The the newest version of fastQC is implemented with threads (each using 
   250 MB).
 - Directory flag is used when the output is a dir.
 - macs2 is added.
 - chrEBV filtered out.
