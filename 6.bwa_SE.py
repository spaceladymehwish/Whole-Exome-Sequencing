
import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()

inst_dir = "bwa"
program_call = "mem"
indices = "/home/bushra/Desktop/Prostate/bwa/genome/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz"
input_dir = "/home/bushra/Desktop/Leukodystrophy/filtered/"
output_sam_dir = "/home/bushra/Desktop/Leukodystrophy/sam/"
cores = " -t 12 "


for x in accessions:
   
    command = inst_dir + " " + program_call + cores + indices + " " + input_dir + x + "_tr.fastq.gz" + " > " + output_sam_dir + x + ".sam"
    print(command + " ....running....")
    os.system(command)

print("All done")
