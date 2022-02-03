#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys

transeq_output=sys.argv[1]
frames=open(transeq_output, "r").readlines()
seq_id=sys.argv[2]

f1="".join(frames).split(">")[1:]

def get_lengths(split_frames):
    lengths=[]
    for seq in split_frames:
        each_frame=seq.split("\n")
        wo_header="".join(each_frame[1:]).rstrip()
        d=wo_header.split("*")
        lengths.append(len(d))
    return lengths

def longest_orf_final(length_of_split, split_frames):
    min_split=length_of_split.index(min(length_of_split))
    Longest_orf=">" + split_frames[min_split]
    return Longest_orf

result=longest_orf_final(get_lengths(f1), f1)

Final="".join(result.split("\n")[1:])

if Final.endswith("*"):
	print(">" + seq_id + "\n" + Final.replace("*",""))
elif "*" in Final:
	x=open(seq_id + "_" + "in_frame_stop_codon.txt", "w")
	seq_nohead=result.split("\n")[1:]
	stop_pos=str(seq_nohead).index("*")
	x.write("In frame stop codon at:" + " " + str(stop_pos))
        x.close()
	print(">" + seq_id + "\n" + Final)
else:
	print(">" + seq_id + "\n" + Final)
