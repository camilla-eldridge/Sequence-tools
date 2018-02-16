
#!/usr/bin/env python

import sys
p=sys.argv[1]
ID=sys.argv[2]

pp=open(p, "r").read()

def phd2fasta(PHD_file):
    splitphd=PHD_file.split("BEGIN_DNA")[1].split("END_DNA")[0]
    SEQ="".join(splitphd.split()[0::3])
    return ">" + ID + "\n" + SEQ

print phd2fasta(pp)
