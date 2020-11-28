#!/usr/bin/env python

import sys


multif=sys.argv[1]
splitn=sys.argv[2]

#multif="test3.fasta"
#splitn=2


fn = open(multif,"r").read()
g=fn.rstrip().split(">")[1:] # split mf fasta file by fasta header >

splitn=int(splitn)


x=[g[i:i+splitn] for i in range(len(g))[::splitn]] # split list by n fasta sequences 

for j, line in enumerate(x,1): # for each 
    c=[k.split("\n") for k in line]  # must split by newline incase of headers with spaces etc...
    new=[">" + "\n".join(p) for p in c] # add removed fasta > symbol to each line (for each new file)
    f = open(str(j) + ".fasta",'w') # Write out files, named by iterator (0,1,2,3.fasta)
    f.write("".join(new)) # write and close file
    f.close()    
    


