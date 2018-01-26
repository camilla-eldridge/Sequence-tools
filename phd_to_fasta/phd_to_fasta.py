
import sys
p=sys.argv[1]
ids=sys.argv[2]

pp=open(p, "r").read()

def trim_read(PHD_file):
    splitphd=PHD_file.split("BEGIN_DNA")[1].split("END_DNA")[0]
    SEQ="".join(splitphd.split()[0::3])
    return ">" + ids + "\n" + SEQ

print trim_read(pp)
