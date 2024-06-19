bam recab --in ~/Desktop/melanoma_WES/Alignment/bwa_mem/dedup/ERR340322_dedup.bam --out ~/Desktop/melanoma_WES/Alignment/bwa_mem/recab/ERR340322_recab.bam --maxBaseQual 40 --refFile ~/Desktop/melanoma_RNASeq/indices/Homo_sapiens.GRCh38.dna.primary_assembly.fa

import os


file = open("acc.txt") #accessions text file
accessions = file.read()
accessions = accessions.split()


inst_dir = "bam recab"
input_dir = "--in ~/Desktop/melanoma_WES/Alignment/bwa_mem/dedup/"
output_dir = "--out ~/Desktop/melanoma_WES/Alignment/bwa_mem/recab/" #output folder, carefully enter the aboslute address
refFile = "--refFile ~/Desktop/melanoma_RNASeq/indices/Homo_sapiens.GRCh38.dna.primary_assembly.fa"
base_qual = "--maxBaseQual 40"


for x in accessions:
   
    command = inst_dir + " " + input_dir + x + "_dedup.bam" + " " + output_dir + x + "_recab.bam" + " " + refFile + " " + base_qual 
    print(command + " ....running....")
    os.system(command)
    print("All done")
