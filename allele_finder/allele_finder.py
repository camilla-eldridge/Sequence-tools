#!/usr/bin/env python 

""" *~~~~*~~~* ALLELE FINDER *~~~*~~~~* """

import sys

input_seq=sys.argv[1]      #"CD63_coding_merged_trimmed.fasta"    #sys.argv[1]        #"CD63_coding_merged_trimmed.fasta"
iD=sys.argv[2]   #"test_cds_"     #sys.argv[2]    #"cd63_cds" #sys.argv[2]  # id in here is gene name and cds or orf 

seqinfo = {}

with open(input_seq, "r") as fasta:
    fasta=fasta.readlines()
    g="".join(fasta).split(">")[1:]
    for seq in g:
        seq=seq.split("\n")
        seq[1]="".join(seq[1:])
        seqinfo.update({seq[0] : seq[1].lower()})
        

variants=list(set(seqinfo.values()))


""" Make a list for each variant to add the others to """
all_alleles=[[i] for i in variants] 



""" Search all query sequences against the unique variants to cluster them""" 
for j in all_alleles:
    for key, value in seqinfo.items():
        if str(value).lower() == "".join(j[0]).lower(): 
            j.append(">" + key + "\n" + value + "\n")
            

""" Save all cluster info to file """
n=0
all_clusters =""
out_table = "cluster" + "," + "n_in_cluster" + "," + "cluster_rep" + "\n"


cluster_members = "Cluster ID" + "," + "Individual" + "\n"

""" Get all cluster members """
for cluster in all_alleles:
    
    all_cluster_ids=""
    each_cluster_ids = ""

    clustr_rep = "".join(cluster[1]).split()[0].replace(">", "")
    z = ("".join(cluster[1:]))   
    x=" ".join(z.split()[0::2]).replace(">", "")
    
    cluster_n=n + 1
    n=cluster_n
    
    for indiv in x.split():
        cluster_members = cluster_members + str(n) + "," + indiv + "\n"

    out_table = out_table + str(n) + "," + str(z.count(">")) + "," + clustr_rep + "\n" 

    """ Leave out first entry of cluster - as it was ref """
    all_clusters = all_clusters + str(n) + "_" +  str(z.count(">")) + "\n" + z + "\n"
    
    

result_table=open(iD + "_cluster_info.txt", "w")
result_table.write(out_table)

cluster_member_out=open(iD + "_cluster_members.csv", "w")
cluster_member_out.write(cluster_members)

out=open(iD + "_clusters" + ".fasta", "w")
out.write(all_clusters) 

