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


''' get node ids and snp pos for sequence 1 only'''

contig_pos=[]

with open(mauve_SNP_output, "r") as snps:      
    each_snp=filter(None, snps.read().split("\n")[1:])
    for j in each_snp:
        j=j.split()
        j12="_".join(str(j[1]).split("_")[0:2])
        contig_pos.append(j12 + "," + j[2] + "," +  j[3])
        

''' Get set of node ids with snps in'''

snp_node_ids=set()

for node in contig_pos:
    snp_node_ids.add(node.split(",")[0])
            

''' Get gbk entries for snp nodes '''

gbk_snp_entries=[]

with open(first_gbk, "r") as gbk:
    
    # split by locus i.e label for contig id
    
    gbk1=gbk.read().split("LOCUS") 
    
    for entry in gbk1:
        at=entry.split("\n")[0].split()
        at2=",".join(at).split(",")[0]
        
        
        for node_id in snp_node_ids:
            if str(node_id) == str(at2):
                gbk_snp_entries.append(entry)
                                

''' Function to find annotated regions for each contig'''

def get_annotations(x):
    contig_cds=[]

    NODEid=x.split()[0]
    
    contig_cds.append(NODEid)
    y = x.split("ORIGIN")[0][1:]
    
    for Q in y.split("\n"):
        to_app=""

        ''' loop through entries, get range '''
        if "rRNA  " in Q  or " CDS " in Q  or  " tRNA " in Q:
            
                to_app = to_app + Q.replace("complement", "").replace("..", " ").replace("(", "").replace(")", "")
        else:
            pass
        
            
        if "/product=" in Q:
            
            to_app = to_app + Q.strip().replace(" ", "_").replace("/", "")
            
        else:
            pass
        
        contig_cds.append(to_app)
        
    contig_cds_strp = [item.strip() for item in contig_cds if item.strip() != '']
    
    return(contig_cds_strp)
    


''' Get annotated entry in each contig '''

all_snp_conts=[]
for C in gbk_snp_entries:
    all_snp_conts.append(get_annotations(C))
    

''' some nodes dont have annotation, contaminants? Print out
remove, replace annotation features to get just pos'''

all_snp_conts_replaced=[]

for E in all_snp_conts:  
    
    nod_id = str(E).split()[0]
    
    if len(E) < 2:  # if no annotated region in the node, print the node id  
    
        print("".join(E) + ": SNP here but no annotations found!")   
        
    else:        
        
        ''' reformat the string, theres probs a better way...
           replace annotation info with node id (we dont need it) ''' 
        
        E=str(E).replace("CDS ", nod_id).replace("tRNA ", nod_id).replace("rRNA ", nod_id).replace("'", "").replace(",", "").replace("[", "").replace("]", "").replace("product=", "").replace('"', "")
        
        ''' remove additional node id info at start and append to final list ''' 
        all_snp_conts_replaced.append([r for r in E.split()[1:]])
    


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


''' input list of snp positions per node, and list of gbk coding regions
iterates through nested lists of snps and annotated regions per node'''

snps_in_annot = {}

for snp_val in snp_node_positions:
    node = snp_val[0]
    snps_in_annot[node] = []
    
    for triplet in all_snp_conts_replaced:
        triplet_node = triplet[0]
        
        if triplet_node == node:
            values = snp_val[1:]
            for i in range(1, len(triplet), 4):
                product = triplet[i + 2]
                range_values = triplet[i:i + 2]
                
                for value in values:
                    int_value = int(value)
                    if int(range_values[0]) <= int_value <= int(range_values[1]):
                        snps_in_annot[node].append({'product': product, 'value': value, 'range': range_values})
                        
                        '''  break the loop here to prevent duplicates ''' 
                        break
                        
        else:
            pass


''' Remove entries with empty key or values 
(these are nodes where snp falls ouside annotated range)'''

snps_in_annot = {k: v for k, v in snps_in_annot.items() if k and v}

for node, entries in snps_in_annot.items():
    print(f"Node: {node}")
    for entry in entries:
        product = entry['product']
        value = entry['value']
        value_range = entry['range']
        print(f"Product: {product}")
        print(f"Value: {value}")
        print(f"Range: {', '.join(value_range)}")
        print("-----")

       
        
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
