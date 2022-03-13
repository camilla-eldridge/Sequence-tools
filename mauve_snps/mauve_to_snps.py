#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: camilla eldridge
"""

import sys

mauve_SNP_output=sys.argv[1]
first_gbk=sys.argv[2]


''' Notes on usage: 
    1. make sure node ids are the same in snp and gbk files 
    2. The gbk file in must be for the first genome input to the progressive
    mauve alignment (snp exporter will output  snps in both genoems but we only use
    the first genome here e.g the SNP file looks like this
    SNP_Pattern	Ref_Contig	Ref_PosInContig	Ref_PosGenomeWide	Assembly_Contig	Assembly_PosInContig	Assembly_PosGenomeWide
    ac	ac	NODE_14	1746	1062759	NODE_16	1746	1060305
    3. Genbank file generated from prokka 1.12 in 2017 '''


contig_pos=[]

with open(mauve_SNP_output, "r") as snps:      
    each_snp=filter(None, snps.read().split("\n")[1:])
    for j in each_snp:
        j=j.split()
        contig_pos.append(j[2] + "," +  j[3])
        



''' Get set of node ids with snps in '''
snp_node_ids=set()

for node in contig_pos:
    snp_node_ids.add(node.split(",")[0])
            


''' Get gbk entries for snp nodes '''
gbk_snp_entries=[]

with open(first_gbk, "r") as gbk:
    
    gbk1=gbk.read().split("LOCUS") # split by locus i.e label for contig id
    
    for entry in gbk1:
        for node_id in snp_node_ids:
            if str(node_id) in entry:
                gbk_snp_entries.append(entry)
                
                
    
''' Function for each contig entry '''
def get_annotations(x):
    contig_cds=[]
    
    NODE=x.split("\n")[0].split()[0]
    contig_cds.append(NODE)
    y = x.split("ORIGIN")[0][1:]
    
    for Q in y.split("\n"):             
        ''' loop through entries, get range '''
        if "rRNA  " in Q  or " CDS " in Q  or  " tRNA " in Q:
            contig_cds.append(Q.replace("complement", "").replace("..", " ").replace("(", "").replace(")", ""))
    
    return(contig_cds)
    
    
    
''' Get range for annotated entry in each contig '''
all_snp_conts=[]
for C in gbk_snp_entries:
    all_snp_conts.append(get_annotations(C))
       
          
''' remove duplicate node id entries from snp list '''
w=[]

for i in contig_pos:
    i=i.split(",")
    nod_id = i[0]
    nod_pos= i[1]
    
    if nod_id not in w:
        w.append("split_me")
        w.append(nod_id)
    else:
        pass
    
    w.append(nod_pos)
    
    
''' get all snp positions for each node '''
snp_node_positions = list(filter(None, [k.split() for k in " ".join(w).split("split_me")]))


''' some nodes dont have annotation, contaminants? Print out, remove, replace annotation features to get just pos'''
all_snp_conts_replaced=[]
for E in all_snp_conts:    
    if len(E) < 2:  # if no annotated region in the node, print the node id    
        print("".join(E) + ": SNP here but no annotations found!")   
    else:        
        ''' reformat the string, theres probs a better way...'''        
        E=str(E).replace("CDS", "").replace("tRNA", "").replace("rRNA", "").replace("'", "").replace(",", "").replace("[", "").replace("]", "")
        all_snp_conts_replaced.append([r for r in "".join(E).split()])
        
      
    
def check_range(range_list, snp_list, Node_ID):    
     ''' check if snp pos is in the range of annotated feature '''     
     snps_out=""     
     range_pairs=[range_list[a:a+2] for a in range(0, len(range_list), 2)]
     
     for ra in range_pairs:  
         for s in snp_list:    
             
             ''' if snp is in range          
             return node id, snp and range '''
             
             if int(s) in range(int(ra[0]), int(ra[1])):        
                 snps_out=snps_out + Node_ID + "," +  s + "," + ":".join(ra) + "\n"
             else:
                 pass
     return(snps_out)
            
        
     
''' check if snps are in annotated range ''' 
for loc in all_snp_conts_replaced:
     nodE=str(loc[0].replace("[", ""))
     
     ''' for each snp found in each node ''' 
     for F in snp_node_positions: 
         
         ''' if node id from snp contigs is the same as node id in the snp list '''     
         if str(F[0]) == nodE:
             
             ''' check if snps ina given node are in the cds/rRNA/tRNA range '''         
             each_check=check_range(loc[1:], F[1:], nodE)         
             print(each_check)
         
         
    
    

''' Notes:
    
    ***sometimes (but not always...)  rRNA entries are like this:
        
        
        so ignored specific feature labels....and located products after....
    
    rRNA            complement(285468..285578)
                     /locus_tag="10580_EscherichiacoliMG1655Sensitive_00595"
                     /product="5S ribosomal RNA"
                     
                     
                     
    sometimes like this:
        
             CDS             complement(267396..268268)
                     /gene="rluF"
                     /locus_tag="10580_EscherichiacoliMG1655Sensitive_00583"
                     /EC_number="5.4.99.21"
                     /inference="ab initio prediction:Prodigal:2.6"
                     /inference="similar to AA sequence:UniProtKB:P32684"
                     /codon_start=1
                     /transl_table=11
                     /product="23S rRNA pseudouridine(2604) synthase"
                     /translation="MLPDSSVRLNKYISESGICSRREADRYIEQGNVFLNGKRATIGD
                     QVKPGDVVKVNGQLIEPREAEDLVLIALNKPVGIVSTTEDGERDNIVDFVNHSKRVFP
                     IGRLDKDSQGLIFLTNHGDLVNKILRAGNDHEKEYLVTVDKPITEEFIRGMSAGVPIL
                     GTVTKKCKVKKEAPFVFRITLVQGLNRQIRRMCEHFGYEVKKLERTRIMNVSLSGIPL
                     GEWRDLTDDELIDLFKLIENSSSEVKPKAKAKPKTAGIKRPVVKMEKTAEKGGRPASN
                     GKRFTSPGRKKKGR"
        
        '''
