#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys

first_gbk=sys.argv[1]
mauve_SNP_output=sys.argv[20]


gbk_1=[] 
with open(mauve_SNP_output, "r") as snps:
    each_snp=snps.readlines()
    for line in each_snp:
        line=line.split()
        gbk_1.append(line[2] + " " + line[3])

final_nodes=[]
headers=[]
for i in gbk_1[1:]:
    nodes="".join(i.split()[0]).split("_length")[0] + " " +  i.split()[1] + "\n"  
    final_nodes.append(nodes)
    header=nodes.split()[0]   
    headers.append(header)
        
head="\n".join(set(headers[1:]))
node_snps=final_nodes[1:]
 
with open(first_gbk, "r") as f:  
    gbk_info=[]     
    f=f.read()
    f=f.split("LOCUS")       
    heads=head.split("\n") 
    for split_heads in heads:
        for lines in f:
            if split_heads in lines:
                gbk_info.append(lines)

cds=""
strings=("gene","CDS ","product") 
for line in gbk_info[1:]:
    line=line.split("\n")  
    Df="".join(line[0].split("DNA")).split()[0]
    for G in line:  
        if "CDS " in G:  
            cds=cds + str(Df) + " " + G.replace("complement", "").replace("(", "").replace(")", "").replace("CDS", "").replace(" ", "").replace(".", " ") + "\n"


def find_in_xrange(iD, snp, rpos1, rpos2):
    cds_snps=""
    CP=xrange(int(rpos1), int(rpos2))
    stpos1=str(rpos1)
    stpos2=str(rpos2)
    if int(snp) in CP:
        cds_snps=cds_snps + iD + " " + "snp:" + snp + " " + "cds:" + " " + stpos1 + " " + stpos2
    elif int(snp) == rpos1:
        cds_snps=cds_snps + iD +  " " + "snp:" + snp + " " + "cds:" + " " + stpos1 + " " + stpos2
    elif int(snp) == rpos2:
        cds_snps=cds_snps + iD + " " + "snp:" + snp + " "  + "cds:" + " "+ stpos1 + " " + stpos2
    else:
        pass
    return cds_snps


cc=cds.replace("\t", " ").replace("\r", " ").replace("  ", " ")
nodes_and_cds=cc[:-1].split("\n") 

coding_snps=[]
save_out=[]
for node_a in node_snps:
    node_a=node_a.split()
    NA=node_a[0]
    SNPS=node_a[1]
    for node_b in nodes_and_cds:
        node_b=node_b.split()
        NB=node_b[0]
        if NA == NB:
            coding_snps.append(find_in_xrange(NA, SNPS, node_b[1], node_b[2]))
      
final_snps=filter(None, coding_snps)            

print("\n".join(final_snps))



