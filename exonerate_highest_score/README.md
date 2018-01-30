exonerate_highest_score.py

Script to get the highest scoring alignment from protein2gneome model in exonerate
from a multifasta file when you dont want to use bestn 1:

Process:

	exonerate --model protein2genome --query test_prot.fasta --target test_genome.fasta  \
	--showalignment no --showvulgar no --showtargetgff yes --bestn 7 \
	--ryo "%qi(%qab -%qae)\n%qas\n >%ti(%tab - %tae):%s\n%tas\n >%ti:%s\n%tcs\n" > test1.exonerate

	extract_exonerate.py  test1.exonerate  gene_id 

	cat *excds* > test_cds.fasta

	exonerate_highest_score.py test_cds.fasta


