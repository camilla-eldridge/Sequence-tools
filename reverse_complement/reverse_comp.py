import sys

input_seq=sys.argv[1]

sequence=open(input_seq, "r").read()

a="".join(sequence.split("\n")[1:])
header=sequence.split("\n")[0]

reverse=a[::-1].lower()

reverse_complement=reverse.replace("a", "T").replace("t","A").replace("c","G").replace("g","C").upper()

print header + "\n" + reverse_complement







