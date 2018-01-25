longest_orf.py

USAGE: python longest_orf.py frames.fasta gene_id > output.fasta 

E.g python longest_orf.py test_frames.fasta test_id > test_output.fasta

- Finds the longest orf from a set of protein translation frames (e.g transeq output) 
- Identifies any in frame stop codons (could be selenocysteine), saves position in a text file
- Finally, removes any stop codons from end of translation if present *Note purposefully does not remove in frame stop 
codons.
