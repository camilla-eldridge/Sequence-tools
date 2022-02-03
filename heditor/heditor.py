
#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys

alignment=sys.argv[1]
output=sys.argv[2]


Final_seq=""

with open(alignment, "r") as f:
    f=f.read()
    g=f.split(">")[1:]
    
    for line in g:
        line=line.split(" ")
        
        if "x" in line: # for hybrid entries - havent tested with x in id name yet.. 
            taxid=line[1:6]
        else:
            taxid=line[1:3]
            
        iD=line[0].split(":")[0]
        seq = "".join(line).split("\n")[1:]
        
        Final_seq = Final_seq + ">" + "_".join(taxid) + "_" + str(iD) + "\n" + "".join(seq) + "\n"
        
Final_seq = Final_seq.replace(",", "").replace("(","").replace(")","").replace(";", "").replace(":", "")   
  
            
out = open(output + ".fasta", "w")    
out.write("".join(Final_seq))
