#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys

input_file=sys.argv[1]
output_file=sys.argv[2]

fasta_file=open(input_file, 'r')  
fasta_lines=fasta_file.read().split('>')[0:]  
unique_sequences=open(output_file,'w')  

def remove_complete_duplicates(fasta_lines): 
    outputlist=[] 
    setofuniqsequence=set()
    for sequence in fasta_lines: 
        if sequence not in setofuniqsequence: 
            outputlist.append(sequence) 
            setofuniqsequence.add(sequence)
    return outputlist

result=remove_complete_duplicates(fasta_lines) 
unique_sequences.write('>'.join(result)) 
unique_sequences.close() 