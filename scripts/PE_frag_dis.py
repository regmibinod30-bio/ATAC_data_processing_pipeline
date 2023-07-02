#!/usr/bin/env python
# PE_frag_dis.py: calculate 4C PE fragment size distribution


import sys

def help():
    print """
# PE_frag_dis.py: calculate size of PE fragments
# usage: .py input > output
#    input: bowtie output
#     HWI-ST1365:101:H7U4UADXX:1:1101:13410:1996 1:N:0:CGAGGC/1 + chrX 25617003 TCCTAGTATTAACTTGTACTAGTTGGTACA C@@FFFDEFHGHHJIJHIJJIJHIIGGHII   0
#     HWI-ST1365:101:H7U4UADXX:1:1101:13410:1996 2:N:0:CGAGGC/2 - chrX 25617019 TACTAGTTGGTACATTTACTCCATCAGTGC JJIIIJIJJJIGJJIIGFJJJHIGIIJJJJ   0
"""

if sys.argv[1] == "-h":
    help()
    sys.exit()


def main():
    with open(sys.argv[1]) as f:
	pos_list = []
	for line in f:
	    new_line = line.strip()
	    items = new_line.split()
	    pos = items[4]
	    if len(pos_list) < 2:
	   	pos_list.append(pos)
	    if len(pos_list) == 2:
 		frag_len = abs(int(pos_list[0]) - int(pos_list[1])) + 50
 		print frag_len
		pos_list = []
	    


if __name__ == '__main__':
    main()

