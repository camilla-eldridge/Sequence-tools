#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: camillaeldridge
"""

import sys

#Given two lists of ID's it prints the IDS not in both files

query = sys.argv[1] #has more ids than test 2 example:test1.txt
target = sys.argv[2] #less ids but they are contained in test1,  example:test2.txt

diff_lines=""

with open(query, "r") as q, open(target, "r") as t:
    q_lines = q.read().split() # list
    t_lines = t.read() #string
    
    # for each id in query file, if its not in the target file save to list
    z=[x for x in q_lines if x not in t_lines]
    
# Print it out in a 'nicer' way ;)...    
for o in z: 
    diff_lines=diff_lines + o + "\n"
    
    
print(diff_lines)   



