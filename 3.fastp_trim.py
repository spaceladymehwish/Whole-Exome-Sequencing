cutadapt -a file:illumina_adapter -o ERR9659988.fastq.gz ERR9659988_trim.fastq.gz

import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()

inst_dir = "fastp"
input_dir = "~/Desktop/melanoma_WES/RAW/"
output_dir = "~/Desktop/melanoma_WES/trim/"
cores = " -w 12 "

for x in accessions:
   
    command = inst_dir + cores + "-i " + input_dir + x + "_1.fastq.gz" + " -I " + input_dir + x + "_2.fastq.gz" + " -o " + output_dir + x + "_trim_1.fastq.gz" + " -O " + output_dir + x + "_trim_2.fastq.gz"
    print(command + " ....running....")
    os.system(command)

print("All done")
