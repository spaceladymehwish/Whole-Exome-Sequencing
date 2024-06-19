
open terminal in melanoma_RNASeq folder, goto alignment then open bam folder 

samtools sort --threads 12 SRR14753170.bam -O or > ~/Desktop/melanoma_RNASeq/Alignment/sorted/SRR14753170_sorted.bam 

import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "samtools sort"
input_dir = "~/Desktop/melanoma_WES/Alignment/bwa_mem/bam/"
output_sorted_bam = "~/Desktop/melanoma_WES/Alignment/bwa_mem/sort/"
cores = " --threads 14 "


for x in accessions:
   
    command = inst_dir + cores + input_dir + x + ".bam" + " -o " + output_sorted_bam + x + "_sorted.bam"
    print(command)
    os.system(command)
    


print("All done")
