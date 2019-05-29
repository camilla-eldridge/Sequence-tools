#!/usr/bin/env python


import sys

ID=sys.argv[1]
infile=sys.argv[2]

imp=open(infile, "r").read()
imp=filter(None, imp.split("\n"))

for i, value in enumerate(imp, 1):
    print ">" + str(i) + "_" + str(ID) + "\n" + value














