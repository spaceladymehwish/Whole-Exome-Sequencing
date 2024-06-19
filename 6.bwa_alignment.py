to build indices for bwa for alignment:

bwa index directory for genome assembly fasta .fa fie - p prefix for indices (indices_genome) file

bwa index ~/Desktop/melanoma_RNASeq/indices/Homo_sapiens.GRCh38.dna.primary_assembly.fa -p indices_genome


to run alignment using bwa mem tool:

bwa mem -t 12 ~/Desktop/melanoma_WES/Alignment/bwa_mem/indices/indices_genome ~/Desktop/melanoma_WES/trim/ERR340322_trim_1.fastq.gz ~/Desktop/melanoma_WES/trim/ERR340322_trim_2.fastq.gz > ~/Desktop/melanoma_WES/Alignment/bwa_mem/sam/ERR340322.sam


to view summary stats of alignment: 

samtools flagstat -@ 12 ~/Desktop/melanoma_WES/Alignment/bwa_mem/sam/ERR340322.sam (input_directory)


import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()

inst_dir = "bwa mem"
input_dir = "~/Desktop/melanoma_WES/trim/"
output_dir = "~/Desktop/melanoma_WES/Alignment/bwa_mem/sam/"
cores = " -t 12"
refFile = "~/Desktop/melanoma_WES/Alignment/bwa_mem/indices/indices_genome"

for x in accessions:
   
    command = inst_dir + cores + " " + refFile + " " + input_dir + x + "_trim_1.fastq.gz" + " " + input_dir + x + "_trim_2.fastq.gz" + " > " + output_dir + x + ".sam"
    print(command + " ....running....")
    os.system(command)

print("All done")