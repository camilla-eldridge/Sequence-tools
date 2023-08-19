mauve_to_snps.py locates if a SNP is within the range of annotated features when given a gbk annotation file and the output of the SNP exporter tool in Mauve.

- Takes the reference (or first) gbk input for progressiveMauve alignment and SNP export file as input. (script will use only the first column of the SNP file)
- Outputs a list of SNPS in annotated regions only (eg. will exclude anything outside the range of annotated tRNA, rRNA or CDS positions but will notify when it encouters a SNP in region with no annotation) 


		USAGE: mauve_to_snps.py Exported_SNPS.txt  first_gbk_file > snps.txt  


Note that this won't be foolproof for mis-annotations!....always check the sequence..
