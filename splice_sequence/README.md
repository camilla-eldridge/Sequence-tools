Extract any sequence with known positions:<br />

    python splice.py  test.fasta  pos.txt  > output.fasta

*Note sequences must be in fasta format, see pos.txt for position file format <br /><br />

Examples of use:
- To get coding exons from an orf
- To get a domain from a protein sequence
- To get nucleotide sequence for a protein domain:
  Change positions in pos.txt: Codon start=(aa position x 3)-2, Codon stop=(aa stopx3) 
