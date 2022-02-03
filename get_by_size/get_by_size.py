#!/usr/bin/python env

"""
@author: camilla eldridge
"""

import sys

multif=sys.argv[1]
splitz=sys.argv[2]

with open(multif, "r") as mf_file:
    g = mf_file.read().rstrip().split(">")[1:]
    for i in g:
        if len("".join(filter(None, i.split("\n")[1:]))) >= int(splitz):
            print(">" + i)
        else:
            pass

