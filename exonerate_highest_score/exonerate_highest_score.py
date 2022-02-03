#!/usr/bin/env python

"""
@author: camilla eldridge
"""


import sys

mf=sys.argv[1]
cdsoutput=open(mf, "r").read().split(">")[1:]

score=[]
for i in cdsoutput:
    b=[]
    f=i.split(":")
    noheader="".join(f[1:]).split("\n")
    score.append(int(noheader[0]))

highest_score_index=score.index(max(score))
lowest_score_index=score.index(min(score))

print(">" + cdsoutput[highest_score_index])



