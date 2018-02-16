#!/usr/bin/env python
import sys

hmm_output=sys.argv[1]
genome_file=sys.argv[2]
model=sys.argv[3] 

with open(genome_file) as genome:
    A=genome.read()
    contigs="".join(A).replace(' ', '')
    each_contig=contigs.split(">")

hmm_result=nome_file=open(hmm_output, 'r').readlines()
c="".join(hmm_result)
if "------ inclusion threshold ------" in c:
    hmm_split=' '.join(hmm_result[15:]).split("  ------ inclusion threshold ------")[0]
else:
    hmm_split=' '.join(hmm_result[15:]).split("Annotation for each hit  (and alignments):")[0]

a=hmm_split.split('\n')[:-3]

hit_sequences=[]

for line in a:
    t=line.split()
    if model == "P":
        ids=str(t[8])
        q=ids.split(',')
        for sequence in each_contig:
            for i in q:
                if i in sequence:
                    hit_sequences.append(">" + sequence)
    else:
        ids=str(t[3])
        q=ids.split(',')
        pos_1=t[4]
        pos_2=t[5]
        P1=pos_1.split(',')
        P2=pos_2.split(',')
        for sequence in each_contig:
            for i in q:
                if i in sequence:
                    cut_header=int(len(i))
                    header=sequence[0:cut_header]
                    no_header=sequence[cut_header:]
                    if int(str(P1[0])) > int(str(P2[0])):
                        hit_sequences.append(">" + header + "\n" + no_header[int(str(P2[0])):int(str(P1[0]))] + "\n")
                    else:
                        hit_sequences.append(">" +  header + "\n" + no_header[int(str(P1[0])):int(str(P2[0]))] + "\n")                   
                            
result="".join(hit_sequences)
print result
   
  
