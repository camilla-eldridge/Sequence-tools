#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

library("ggplot2")
library("gridExtra")
library("ggpubr")

intron_lens<-args[1]
exon_lens<-args[2]
gene_lens<-args[3]
perc_support<-args[4]

#Plot intron length dist.
intL<-data.frame(read.table(intron_lens, header = FALSE))
attach(intL)
Log_intLen<-ggplot() + geom_histogram(aes(log(intL$V1)), bins = 1000, fill = "blue") + geom_density(alpha = 0.4) + theme_classic() + labs(x ="Intron length(bp)", y = "Count") #title="Distribution of intron lengths (log)"
Intron_len<-ggplot() + geom_histogram(aes(intL$V1), bins = 1000, fill = "blue") + geom_density(alpha = 0.4) + theme_classic() + labs(x ="Intron length(bp)", y = "Count") # title="Distribution of intron lengths"
detach(intL)

# Plot exon length dist.
exL<-data.frame(read.table(exon_lens, header = FALSE))
attach(exL)
Log_exonLen<-ggplot() + geom_histogram(aes(log(exL$V1)), bins = 1000, fill = "blue") + geom_density(alpha = 0.4) + theme_classic() + labs(x ="Exon length(bp)", y = "Count")#title="Distribution of exon lengths (log)"
Exon_len<-ggplot() + geom_histogram(aes(exL$V1), bins = 1000, fill = "blue") + geom_density(alpha = 0.4) + theme_classic() + labs(x ="Exon length(bp)", y = "Count") #title="Distribution of exon lengths"
detach(exL)

#Plot gene length dist.
genL<-data.frame(read.table(gene_lens, header = FALSE))

attach(genL)
Log_geneLen<-ggplot() + geom_histogram(aes(log(genL$V1)), bins = 1000, fill = "blue") + geom_density(alpha = 0.4) + theme_classic() + labs(x ="Gene length(bp)", y = "Count") #title="Distribution of gene lengths (log)"
Gene_len<-ggplot() + geom_histogram(aes(genL$V1), bins = 1000, fill = "blue") + geom_density(alpha = 0.4) + theme_classic() + labs(x ="Gene length(bp)", y = "Count") #title="Distribution of gene lengths"
detach(genL)

#Plot transcript support from augustus.
perc<-data.frame(read.table(perc_support, header = FALSE))
attach(perc)

#Plot all support.
all_support<-ggplot() + geom_histogram(aes(perc$V3), fill = "blue", bins = 100) + geom_density(alpha = 0.4) + theme_classic() + labs(x ="% support", y = "Count")#title="Distribution of transcript support (all sources) ",

#Plot intron support.
intron_support<-ggplot() + geom_histogram(aes(perc$V4), fill = "blue", bins = 100) + geom_density(alpha = 0.4) + theme_classic() + labs(x ="% support", y = "Count")#title="Distribution of transcript support - Introns ",

res <- marrangeGrob(list(Gene_len, Exon_len, Log_geneLen, Log_exonLen, Intron_len, all_support, Log_intLen, intron_support), nrow = 2, ncol = 2)

# Export to a pdf file
ggexport(res, filename = "braker_stats.pdf")

