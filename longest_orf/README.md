
Script to:
- Find the longest orf from a set of protein translation frames (e.g transeq output) 
- Identify any in frame stop codons (could be selenocysteine, saves position in a text file)
- Finally, removes any stop codons from end of translation if present *Note purposefully does not remove in frame stop 
codons.

    python  longest_orf.py  test_frames.fasta  test_id  >  output.fasta 

