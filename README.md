# Sequence tools 



This is a repository of sequence tools written in Python: <br /> <br /> <br /> <br /> 

	replace_heads.py

Given a txt file of new headers, replaces existing headers in an mf file.<br /> <br /> <br />

	heditor.py

Edits Genbank headers to include species name and accession number only.<br /> <br /> <br />

	find_seq_overlap.py

Gets position of overlapping sequences on a given target sequence.<br /> <br /> <br />

	gbk_to_proteome.py
Gets all protein sequences from a gbk file.  <br /> <br /> <br /> 
										
	 splice.py
To get sequence based on positions. <br /> <br /> <br /> 

	longest_orf.py
To find the longest orf from all frames and identify presence of in-frame stop codons. <br /> <br /> <br />

	get_seq_go.py
Get sequence from a multifasta file based on id. <br /> <br /> <br /> 

	reverse_complement.py
Reverse complements a sequence. <br /> <br /> <br /> 

	phd_to_fasta.py
Gets fasta sequence from phd file. <br /> <br /> <br /> 

	mulif_to_singlef.py
Separates multi fasta file to single fasta files. <br /> <br /> <br />

	remove_duplicate_fasta.py
Removes identical sequences (with identical headers). <br /> <br /> <br /> 

	extract_exonerate_output.py
Separates exonerate output into gff, orf and cds. <br /> <br /> <br /> 

	exonerate_highest_score.py
Gets highest scoring sequence alignment from exonerate output (when you don't want to use bestn). <br /> <br /> <br />

	nhmmer_or_hmmsearch_to_fasta.py
Gets fasta sequence for protein hits from hmmsearch or hit regions(dna) from nhmmer.  <br /> <br /> <br />

	unique_headers.py	
Removes characters ":,.()%*" from fasta file headers, truncates header after first white space and adds a unique id. <br /> <br /> <br />

	unique_ids.py
Removes existing headers in a fasta file and replaces them with unique ids for each sequence ( >1, >2, >3 ...) <br /> <br /> <br />

	split_fasta_ntimes.py

Splits multi-fasta file into smaller multi-fasta files by N sequences <br /> <br /> <br />

	get_by_size.py
	
Extracts all sequences from an mf file that are >= a desired length. <br /> <br /> <br />

	compare_txt.py

Compares two text files (e.g can use to compare accession ids) and prints any ids that are not in both text files.


## Future use 
This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0), this means you can share and adapt this code but you must give the original author credit and indicate any modifications made.
