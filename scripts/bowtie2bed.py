#!/usr/bin/env python
# bowtie2bed.py: create a bed file out of a bowtie output


import sys, os

def help():
    print """
# bowtie2bed.py: create a bed file out of a bowtie output
# usage: .py bowtie_out > bed
#        specifically tailored to make input files for make-graph-file.py
# related programs: bowtie, run-graph.py, make-graph-file.py, run-make-graph-file-by-chrom.py
# need python 2.7.6 or above (include "module load python/2.7.6;" in a swarm file

"""

if sys.argv[1] == "-h":
    help()
    sys.exit()

#input = open(sys.argv[1], "r").readlines()

with open(sys.argv[1]) as f:
    for line in f:
	new_line = line.strip()
	items = new_line.split()
	chr, start, end, U, strand = items[3], items[4], int(items[4])+len(items[5])-1, len(items[5]), items[2]
	print chr, "\t", start, "\t", end, "\t", U, "\t", 0, "\t", strand

