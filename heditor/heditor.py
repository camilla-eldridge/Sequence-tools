
#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys

alignment=sys.argv[1]
output=sys.argv[2]


#alignment="test2.fasta"
#output="test2out-new"

final_seq=""
new_list=""

with open(alignment, "r") as f:
    f=f.read()
    g=f.split("\n")
    
    for line in g:
       line=line.split()
       new_list=new_list + " ".join(line).replace(">", "*", 1) + "\n" 
       

x=filter(None, new_list.split("*"))

for k in x:
       
    t=k.split("\n")
    head=t[0]
    head=head.split()
    
    taxid=" ".join(head[1:3])
    iD=head[0].split(":")[0]
    seq=t[1]
    
    final_seq = final_seq + ">" + "".join(taxid) + "_" + str(iD) + "\n" + "".join(seq) + "\n"
                  
out = open(output + ".fasta", "w")    
out.write("".join(final_seq))
