allele_finder.py  <br /> <br /> <br /> 

- Given multi-fasta file, sorts sequences into identical groups (can be used to cluster any strings in fasta format by 100% id)

- Returns tables of counts and cluster ids for plotting and further analysis. <br /> <br /> <br /> 



         USAGE: allele_finder.py mf_file id


         Example: allele_finder.py test.fasta test


 <br /> <br /> <br /> 
 
Output: <br /> <br /> <br /> 

test_clusters.fasta  

Sequence file sorted into indentical cluster groups, n in cluster shown in header.  <br /> <br /> <br /> 

test_cluster_info.txt  

table of cluster members, n in cluster and cluster representative id    <br /> <br /> <br /> 

test_cluster_members.csv  

table of cluster ids per individual   <br /> <br /> <br /> 
