#!/usr/env python
import sys

gbk=sys.argv[1]

final=""
with open(gbk, "r") as f:
    f=f.read()
    f=f.split("CDS")  ### split by CDS entry, each CDS has 1 protein entry ###
    for r in f:
        if 'product="' in r:  #### make sure product is in each entry before split - stops index error ###
            if "translation=" in r:  #### make sure only splitting the protein containing entries - stops index error###
             k=r.split('product=')[1]   ### take product line == protein id ###split by translation ###
             head=k.split('"')[1].replace("\n", "").replace("  ", "") ## make sure any long protien id's are not separated by lines ##
             z=k.split('translation="')[1].split('"')[0]  ### split by "translation=" and '"' to get just protein sequence ###
             final=final + (">" + "".join(head) + "\n" + z.replace(" ", "") + "\n") ### save each header and protein sequence ##

final=final.replace("\n\n", "\n") ## remove any new lines ##
print(final)                

