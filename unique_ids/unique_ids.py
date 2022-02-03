#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys

multif=sys.argv[1]
outf=sys.argv[2]

fn=open(multif,"r").read()
g=fn.split(">")[1:]
out=open(outf, "w")

saved=""
for j, line in enumerate(g):
    id=j+1
    t=line.split()
    k="".join(line).split("\n")
    seq="".join(k[1:]).rstrip()
    saved=saved + ">" + str(id) + "\n" + seq + "\n"
out.write(saved)

