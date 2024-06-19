import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()

inst_dir = "fastqc"
input_dir = "~/Desktop/melanoma_WES/trim/"
output_dir = "~/Desktop/melanoma_WES/QC/final/"

for x in accessions:
   
    command = inst_dir + " " + input_dir + x + "_trim.fastq.gz" + " -o " + output_dir
    print(command + " ....running....")
    os.system(command)

print("All done")

or command: fastqc *_trim_1.fastq.gz
and then command fastqc*_trim_2.fastq.gz