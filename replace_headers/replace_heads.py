#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys

mf=sys.argv[1]
new_heads=sys.argv[2]
output=sys.argv[3]


with open(new_heads, "r") as headers:
    headers = headers.read().split()
    
    
seq=[]

with open(mf, "r") as f:
    f=f.read()
    f=f.split(">")[1:]
    for line in f:
        line=line.split(" ")
        seq.append("\n".join("".join(line).split("\n")[1:]))
        

final = ["\n".join(a) for a in zip(headers, seq)]

out = open(output, "w")
out.write("".join(final))

        
