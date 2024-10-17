#!/usr/bin/env python

"""
@author: camilla eldridge
"""

import sys
import re
from typing import List

def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

def find_epitopes_in_sequence(sequence: str, epitopes: List[str]) -> str:
    a = "".join(sequence).split("\n")[1]
    pos = ""

    for i in epitopes:
        matches = re.finditer(r'(?=(%s))' % re.escape(i), a)
        pos += str([('%01d %01d %s' % (m.start(1), m.end(1), m.group(1))) for m in matches]) + "\n"
    
    return pos

def process_epitopes_file(epi: str) -> List[str]:
    with open(epi, "r") as epitopes:
        lines = epitopes.readlines()
        e = "".join(lines).split("\n")[1::2]
        return e

def main(seq: str, epi: str, out: str) -> None:
    sequence = read_file(seq)
    with open(out, "w") as positions:
        epitopes = process_epitopes_file(epi)
        pos = find_epitopes_in_sequence(sequence, epitopes)

        k = pos.replace("[]", "").replace("[", "").replace("]", "").replace("'", "")
        positions.write("".join(k))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python find_seq_overlap.py sequence_file epitope_file output_file")
        sys.exit(1)
    seq = sys.argv[1]
    epi = sys.argv[2]
    out = sys.argv[3]
    main(seq, epi, out)
