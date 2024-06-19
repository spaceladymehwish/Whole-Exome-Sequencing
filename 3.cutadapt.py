
import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()

inst_dir = "cutadapt"
input_dir = "/home/mehwish/Desktop/4_Alzheimers_multiomics/Alzheimers_miRNA_rnaseq/raw/"
output_dir = "/home/mehwish/Desktop/4_Alzheimers_multiomics/Alzheimers_miRNA_rnaseq/trim_cutadapt/"
adapter_dir = "/home/mehwish/Desktop/4_Alzheimers_multiomics/Alzheimers_miRNA_rnaseq/illumina_adapter"



for x in accessions:
   
    command = inst_dir + " -a file:" + adapter_dir + " " + input_dir + x + ".fastq.gz" + " -o " + output_dir + x + "_trim.fastq.gz"
    print(command + " ....running....")
    os.system(command)

print("All done")
