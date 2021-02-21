#!/usr/bin/python env

import sys

multif=sys.argv[1]
splitsize=sys.argv[2]

fn = open(multif,"r").read()
g=fn.rstrip().split(">")[1:] # split mf fasta file by fasta header >

splitz=int(splitsize)

for i in g:
    seq="".join(filter(None, i.split("\n")[1:]))
    if len(seq) >= splitz:
        out=">" + i
        print(out)
