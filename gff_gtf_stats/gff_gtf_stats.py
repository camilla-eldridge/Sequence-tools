#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Created on Sun Jul 18 18:03:40 2021
@author: camilla eldridge
"""

import sys
#from statistics import median

gff_file=sys.argv[1]  
gtf_file=sys.argv[2]
ID=sys.argv[3]


with open(gtf_file, "r") as gtf_in:
    c=gtf_in.readlines()
""" read in gtf file(augustus.final.hints.gtf """
    

def write_out(string_name, iD, to_write):
    """ write out function for txt files """ 
    with open(str(iD) + str(string_name), 'w') as f:
                  for item in to_write:
                      f.write("%s\n" % item)
            

s="".join(c).replace("gene_id", "Gid")
print("N genes:" + str(s.count("gene")))
""" get and print out number of genes """


def get_lens(strng,thing):
    """ function to get intron and exon lens """
    out_list=[]
    for h in thing:
        h=h.split()
        if str(strng) in h:
            out=int(h[4]) - int(h[3])
            out_list.append(out)
    return(out_list)
    
    
intron_lens=get_lens("intron", c)
exon_lens=get_lens("exon", c)
""" get all intron and exon lens for every transcript """
    

write_out("_intron_lens.txt", ID, intron_lens)
write_out("_exon_lens.txt", ID, exon_lens)
""" write out intron and exon lens """


print("average exon length:" + str(int(sum(exon_lens) / len(exon_lens))))
print("average intron length:" + str(int(sum(intron_lens) / len(intron_lens))))
print("Min exon len:" + str(min(exon_lens)))
print("Max exon len:" + str(max(exon_lens)))
print("Min intron len:" + str(min(intron_lens)))        
print("Max intron len:" + str(max(intron_lens)))     
print("N total introns:" + str(len(intron_lens)))        
print("N total exons:" + str(len(exon_lens))) 
""" print a load of stats, weee """       
   

with open(gff_file, "r") as gff_in:
    d=gff_in.readlines()
""" read in gff file (augustus.hints.gff) """
    
   
gene_split="".join(d).split("# start gene")[1:]
""" split by gene entry """


start_codons=str(gene_split).count("start_codon")
print("N start codons:" + str(start_codons))
stop_codons=str(gene_split).count("stop_codon")
print("N stop codons:" + str(stop_codons))
""" find number of start and stop codons """


singles=str(gene_split).count("single")
print("N single exon transcripts:" + str(singles))
""" get number of single exon genes, based on 
where 'single' string appears
"""

full_transcripts=[]
""" identify full length transcripts based on 
presence of both start and stop codons in entry"""

for n in gene_split:
    n=n.split()
    if "start_codon" and "stop_codon" in n:
        full_transcripts.append(n[0])

 
len_full_trans=len(full_transcripts)
print("N transcripts with start and stop:" + str(len_full_trans))

""" get and print number of full length transcripts """


def find_conf(x_split):
    """ get perc confidence based on any source used in augustus 
    for introns and exons - info from gff intermediate file
    """
    x_split2=x_split[0]
    
    if int(x_split2) == 0:
        """ if there is no evidence used e.g 0, confidence = 0 """
        conf=0
    
    else:
        """ divide the fraction for a perc or leave as 0 ... e.g
        0/2 is left at 0, 2/4 is 50% entries look like:
        # # e.g CDS introns: 7/7    """
        conf=str((int(x_split2)/int(x_split[1])) * 100)
    return(conf)   
    

gene_lens=[]
""" list of gene lens """


perc_support=[]
""" Perc support for each trancript on each scaffold """

for i in gene_split:
    i = i.split("\n")    
    k = "".join(i).split("% of transcript supported by hints (any source):")[1].split("#")[0]
    j=(i[1].split())
    
    """ perc introns supported per transcript by rna-seq """
    int_con="".join(i).split("CDS introns:")[1].split("#")[0]
    in_split=int_con.split("/")
        
    """ perc introns supported per transcript by rna-seq """
    ex_con="".join(i).split("CDS exons:")[1].split("#")[0]
    ex_split=ex_con.split("/")
     
    """ append all info into final list for perc support """
    perc_support.append(j[0] + " " + j[8] + " " + k + " " + str(find_conf(in_split)) + " " + str(find_conf(ex_split)) + " " + str(int_con) +  " " + str(ex_con) )
   
    """ get gene lens and add to list for each model """
    gene_len=int(j[4]) - int(j[3])
    gene_lens.append(gene_len)   
    
            
write_out("_gene_lens.txt", ID, gene_lens)
write_out("_perc_support.txt", ID, perc_support)  
""" write out txt files """       

print("average gene len:" + str(int(sum(gene_lens) / len(gene_lens))))
""" print out av gene len """

