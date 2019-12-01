#!/usr/bin/env python

import sys

iD=sys.argv[1]
ffile=sys.argv[2]

with open(ffile, "r") as fasta:
    fasta=fasta.readlines()
    seq="".join(fasta[1:]).replace("\n", "").upper() + "*"
    ali=">P1;" + str(iD) + "\n" + "sequence:" + str(iD) + ":::::::0.00: 0.00" + "\n" + seq
    print ali

