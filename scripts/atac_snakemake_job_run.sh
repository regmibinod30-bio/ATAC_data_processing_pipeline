#!/bin/bash
module load snakemake/6.8.2; 
snakemake -s hg38_Snakefile -j 150 --latency-wait 60 --cluster-config=cluster.yml --cluster "sbatch --gres=lscratch:40 --time=008:00:00 --cpus-per-task={threads} --mem={params.mem} --partition={cluster.partition} " 2>snake.error
