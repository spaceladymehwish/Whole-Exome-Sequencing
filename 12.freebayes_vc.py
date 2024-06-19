freebayes -f ~/Desktop/melanoma_RNASeq/indices/Homo_sapiens.GRCh38.dna.primary_assembly.fa ~/Desktop/melanoma_WES/Alignment/bwa_mem/recab/ERR340322_recab.bam > ~/Desktop/melanoma_WES/variant_calling/free_bayes/ERR340322.vcf


import os


file = open("acc.txt") #accessions text file
accessions = file.read()
accessions = accessions.split()


inst_dir = "freebayes"
input_dir = "~/Desktop/melanoma_WES/Alignment/bwa_mem/dedup_recab_combined/"
output_dir = "~/Desktop/melanoma_WES/variant_calling/dedup_recab_combined_freebayes/" #output folder, carefully enter the aboslute address
refFile = "-f ~/Desktop/melanoma_RNASeq/indices/Homo_sapiens.GRCh38.dna.primary_assembly.fa"



for x in accessions:
   
    command = inst_dir + " " + refFile + " " + input_dir + x + ".bam" + " > " + output_dir + x + ".vcf" + " " 
    print(command + " ....running....")
    os.system(command)
    print("All done")
