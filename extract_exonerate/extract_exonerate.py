#!/usr/bin/env python

"""
@author: camilla eldridge
"""


import sys

exonerate_output=sys.argv[1]
gene_id=sys.argv[2]

multif=open(exonerate_output,"r").read()
g=multif.split("##gff-version")[1:]
ids=exonerate_output.split("_")[0]

identity=""
for i in g:
    t=i.split(">")
    gff=t[0]
    gene=t[1]
    cds=t[2].replace("-- completed exonerate analysis", "").replace("# --- START OF GFF DUMP ---", "").replace("#","")
    cd=cds.split(">")
    ids="".join(cd).split("\n")[0].split()
    identity=identity + ":" + ("".join(ids)) + ";"
    iii=identity.split(":")
    dd=list(enumerate(iii))[1:]
    ee=''.join(map(str,dd)).split(";")[:-1]
    ge=gene.split(">")
    gf=gff.split("##source-version") 
    for yu in ee:
        tt=yu.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace('"', "").replace(" ", "_") #formats the string..
    for v in gf:
        f=open(gene_id + "_" + "".join(tt) + ".gff", "w")
        f.write(v)
        f.close()
    for a in ge:
        f1=open(gene_id + "_" + "".join(tt) + "_orf.fasta", "w")
        f1.write(">" + a)
        f1.close()
    for b in cd:
        f2=open(gene_id + "_" + "".join(tt) + "_excds.fasta", "w")
        f2.write(">" +  b)
        f2.close()
