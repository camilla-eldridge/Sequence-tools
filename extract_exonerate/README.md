Separates exonerate output from the following command:

      exonerate --model protein2genome --query test_prot.fasta --target test_genome.fasta \
      --showalignment no --showvulgar no --showtargetgff yes --bestn 5  \
      --ryo "%qi(%qab -%qae)\n%qas\n >%ti(%tab - %tae)\n%tas\n >%ti\n%tcs\n" > test.exonerate 
   
<br />

    python   extract_exonerate.py  test.exonerate   gene_id 



