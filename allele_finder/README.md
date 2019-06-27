allele_finder.py 

Given multi-fasta file, sorts sequences into putative alleles and returns tables for plotting and further analysis. 


USAGE: allele_finder,py mf_file id


Example: allele_finder.py test.fasta test


Output:

test_clusters.fasta 

Sequence file sorted into indentical cluster groups, n in cluster shown in header. 

test_cluster_info.txt  

table of cluster members, n in cluster and cluster representative id   

test_cluster_members.csv  

table of cluster ids per individual  
