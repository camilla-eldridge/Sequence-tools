mauve_to_snps.py locates the SNP range when given a gbk annotation file and the output of the SNP exporter tool in Mauve


- Takes the reference (or first) gbk input for progressiveMauve alignment and SNP export file as input.
- Outputs a list of snps in annotated regions only (will exclude anything outside the range of annotated tRNA, rRNA or CDS positions eg.excludes SNPS from non target species).


		USAGE: mauve_to_snps.py Exported_SNPS.txt  first_gbk_file > snps.txt  
