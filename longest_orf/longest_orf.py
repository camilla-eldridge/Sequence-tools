#!/usr/bin/env python

"""
@author: Camilla Eldridge
@description: A script to find the longest open reading frame (ORF) from a translated nucleotide sequence.
@usage: python longest_orf.py <transeq_output> <seq_id> > longest_orf.faa
"""

import sys
from typing import List

''' splits each translated frame by stop codons'''
def get_lengths(split_frames: List[str]) -> List[int]:
    lengths: List[int] = []
    for seq in split_frames:
        each_frame: List[str] = seq.split("\n")
        wo_header: str = "".join(each_frame[1:]).rstrip()
        d: List[str] = wo_header.split("*")
        lengths.append(len(d))
    return lengths

''' finds the transaltion with the minimum no of splits '''
def longest_orf_final(length_of_split: List[int], split_frames: List[str]) -> str:
    min_split: int = length_of_split.index(min(length_of_split))
    Longest_orf: str = ">" + split_frames[min_split]
    return Longest_orf

''' check the number of input vars'''
def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python longest_orf.py <transeq_output> <seq_id>")
        sys.exit(1)

transeq_output: str = sys.argv[1]
seq_id: str = sys.argv[2]

try:
    frames: List[str] = open(transeq_output, "r").readlines()
except IOError:
    print(f"Error: Cannot open file {transeq_output}")
    sys.exit(1)

''' split to remove headers, get the longest orf'''
f1: List[str] = "".join(frames).split(">")[1:]
result: str = longest_orf_final(get_lengths(f1), f1)
Final: str = "".join(result.split("\n")[1:])

''' If there is an in-frame stop codon, print the postion in a newfile'''
if Final.endswith("*"):
    print(">" + seq_id + "\n" + Final.replace("*",""))
elif "*" in Final:
    with open(seq_id + "_" + "in_frame_stop_codon.txt", "w") as x:
        seq_nohead: List[str] = result.split("\n")[1:]
        stop_pos: int = str(seq_nohead).index("*")
        x.write("In frame stop codon at:" + " " + str(stop_pos))
    print(">" + seq_id + "\n" + Final)
else:
    print(">" + seq_id + "\n" + Final)
    

if __name__ == "__main__":
    main()
