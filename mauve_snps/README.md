SNP exporter tool in Mauve gives you location of SNPs in contigs but this doesn't tell you which protein/rna. 

mauve_snps.py locates the SNP when given a gbk annotation file:



- Takes the reference (or first) gbk input for progressiveMauve alignment and SNP export file as input.
- Outputs a list of snps in annotated regions.


		USAGE: mauve_snps.py  first_gbk_file  Exported_SNPS.txt > snps.txt  
