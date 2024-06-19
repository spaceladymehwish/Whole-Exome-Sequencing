build indices for bowtie2

bowtie2-build ref genome path prefix for indices

bowtie2-build ~/Desktop/melanoma_RNASeq/indices/Homo_sapiens.GRCh38.dna.primary_assembly.fa indices_genome


import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "bowtie2"
indices = "~/Desktop/melanoma_WES/Alignment/bowtie2/indices/"
input_dir = "~/Desktop/melanoma_WES/trim/"
output_sam_dir = "~/Desktop/melanoma_WES/Alignment/bowtie2/sam/"
cores = " -p 14"


for x in accessions:
   
    command = inst_dir + cores + " -x " + indices + " -1 "  + input_dir + x + "_trim_1.fastq.gz" + " -2 " + input_dir + x + "_trim_2.fastq.gz" + " -S " + output_sam_dir + x + ".sam"
    print(command + " ....running....")
    os.system(command)
    


print("All done")
