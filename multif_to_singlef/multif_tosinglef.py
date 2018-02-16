#!/usr/bin/env python

import sys

multif=sys.argv[1]
fn = open(multif,"r").read()
g=fn.split(">")[1:]

for j, line in enumerate(g):
    t=line.split()   
    k="".join(line).split("\n")
    header="".join(k[0]).rstrip()
    seq="".join(k[1:]).rstrip()
    f = open(header + "_" + str(j) + ".fasta",'w')
    f.write(">" + header + "\n" +  seq)
    f.close()
