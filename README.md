Some useful sequence tools written in python 2.7:<br /> <br /> <br /> <br /> 

	gbk_to_proteome.py
Gets all protein sequences from a gbk file  <br /> <br /> <br /> 

	mauve_snps_to_cds.py
Identifies which SNPS exported from mauve are in coding regions <br /> <br /> <br /> 
															
	 splice.py
To get any sequence based on positions <br /> <br /> <br /> 

	longest_orf.py
To find the longest orf from a set of frames and identify presence of in frame stop codons <br /> <br /> <br />

	get_seq_go.py
Get sequence from a multifasta file based on id <br /> <br /> <br /> 

	reverse_complement.py
Reverse complements a sequence <br /> <br /> <br /> 

	phd_to_fasta.py
Gets fasta sequence from phd file <br /> <br /> <br /> 

	mulif_to_singlef.py
Separates multi fasta file to single fasta files <br /> <br /> <br />

	remove_duplicate_fasta.py
Removes identical sequences (with identical headers) <br /> <br /> <br /> 

	extract_exonerate_output.py
Separates exonerate output into gff, orf and cds <br /> <br /> <br /> 

	exonerate_highest_score.py
Gets highest scoring sequence alignment from exonerate output (when you don't want to use bestn) <br /> <br /> <br />

	nhmmer_or_hmmsearch_to_fasta.py
Gets fasta sequence for protein hits from hmmsearch or hit regions(dna) from nhmmer  <br /> <br /> <br />

	unique_headers.py	
Removes characters ":,.()" from fasta file headers, truncates header after first white space and adds a unique id.
