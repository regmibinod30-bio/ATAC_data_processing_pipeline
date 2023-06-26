#!/usr/bin/env python
# HW Sun & HY Shih NIAMS

import sys

def help():
    print """
# bowtie_size.py: PE fragment size based bowtie filtering
# HW Sun & HY Shih, NIAMS
# usage: .py input size_low size_high > output
#    input: bowtie output
#     HWI-ST1365:101:H7U4UADXX:1:1101:13410:1996 1:N:0:CGAGGC/1 + chrX 25617003 TCCTAGTATTAACTTGTACTAGTTGGTACA C@@FFFDEFHGHHJIJHIJJIJHIIGGHII   0
#     HWI-ST1365:101:H7U4UADXX:1:1101:13410:1996 2:N:0:CGAGGC/2 - chrX 25617019 TACTAGTTGGTACATTTACTCCATCAGTGC JJIIIJIJJJIGJJIIGFJJJHIGIIJJJJ   0
# last modified: 10/25/14, 6/10/14
"""

if sys.argv[1] == "-h":
    help()
    sys.exit()

if len(sys.argv) < 4:
   print "##### Need 3 inputs!!! #####"
   sys.exit()

input_file = sys.argv[1]
low = int(sys.argv[2])
high = int(sys.argv[3])

def main():
	pos_list = []
        line_list = []
	for line in open(input_file):
	    new_line = line.strip()
	    items = new_line.split()
	    pos = items[4]
	    if len(pos_list) < 2:
	   	pos_list.append(pos)
                line_list.append(line)
	    if len(pos_list) == 2:
 		frag_len = abs(int(pos_list[0]) - int(pos_list[1])) + 50
                if low < frag_len <= high:
		    #print frag_len
                    #print line_list
		    for a in line_list:
			print a,
 		
		pos_list = []
		line_list = []
	    


if __name__ == '__main__':
    main()

