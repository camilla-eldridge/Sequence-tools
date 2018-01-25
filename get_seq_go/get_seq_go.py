import sys
ids=sys.argv[1]
genome_file=sys.argv[2]

input_ids=open(ids, "r").readlines()
X="".join(input_ids).split()

seq=""
with open(genome_file) as genome:
    each_contig="".join(genome).split(">")
    for line in each_contig:
        head=line.split("\n")[0]
        for i in X:
            if i == head:
                seq=seq + ">" + line
	    else:
		pass

print seq.rstrip()
