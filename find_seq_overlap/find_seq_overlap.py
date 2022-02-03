#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys
import re

seq=sys.argv[1]
epi=sys.argv[2]
out=sys.argv[3]


sequence=open(seq, "r").read()
positions=open(out, "w")

a="".join(sequence).split("\n")[1] 


pos=""

with open(epi) as epitopes:
    epitopes = epitopes.readlines()
    for line in epitopes:
    
        """ Remove epitope headers """
        e=("".join(epitopes).split("\n")[1::2])
        
        for i in e:
            
                """ Find epitope in sequence (overlapping or not) """
                matches=re.finditer(r'(?=(%s))' % re.escape(i),a) 
                
                """Get start:stop positions for epitopes and corresponding sequence"""
                pos=pos  +  str([('%01d %01d %s' % (m.start(1), m.end(1), m.group(1))) for m in matches]) + "\n"   
        
        break

k=pos.replace("[]", "").replace("[", "").replace("]", "").replace("'", "")

positions.write("".join(k))






