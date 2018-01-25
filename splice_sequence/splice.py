#!/usr/bin/env python
import sys

seq_fasta=sys.argv[1]
pos_txt=sys.argv[2]

sequence=open(seq_fasta, "r").read()
positions=open(pos_txt, "r").readlines()

split=sequence.split("\n")
seq="".join(split[1:])
head=split[0]

cds=""

for line in positions:
    each_cds=line.split()
    pos1=each_cds[0]
    pos2=each_cds[1]
    cds=cds + str(seq[int(pos1)-1:int(pos2)])

print head + "\n" + (cds.replace("\n",""))
