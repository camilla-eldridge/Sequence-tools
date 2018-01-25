Extract any sequence with known positions

USAGE: sequence.fasta positions.txt > output.fasta

e.g
python splice.py test.fasta pos.txt > out.fasta 

*Note sequences must be in fasta format, see pos.txt for position file format 

Examples of use:
- To get coding exons from an orf
- To get a domain from a protein sequence
- To get nucleotide sequence for a protein domain:
  Change positions in pos.txt:
  Codon start=(aa position x 3)-2
  Codon stop=aa stop  
