import sys

multif=sys.argv[1]
outf=sys.argv[2]

fn=open(multif,"r").read()
g=fn.split(">")[1:]
out=open(outf, "w")

saved=""
for j, line in enumerate(g):
    t=line.split()
    k="".join(line).split("\n")
    header="".join(k[0]).rstrip().split(" ")[0].replace(".", "").replace(",", "").replace("(","").replace(")","").replace(";", "").replace(":", "").replace("|", "").replace("*", "")
    seq="".join(k[1:]).rstrip()
    saved=saved + ">" + header + "_id" + str(j) + "\n" + seq + "\n"
out.write(saved)


#replaces unwanted characters and gives unique id to each sequence
#puts in "id" before number to stop confusion with accession ns
