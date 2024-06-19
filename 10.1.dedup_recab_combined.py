
bam dedup --recab --in input.bam --out output.bam --refFile reference --oneChrom --storeQualTag OQ --maxBaseQual 40 

bam dedup --recab --in ~/Desktop/melanoma_WES/Alignment/bwa_mem/sort/ERR340326_sorted.bam --out ~/Desktop/melanoma_WES/Alignment/bwa_mem/dedup_recab_combined/ERR340326.bam --refFile ~/Desktop/melanoma_RNASeq/indices/Homo_sapiens.GRCh38.dna.primary_assembly.fa --oneChrom --storeQualTag OQ --maxBaseQual 40


import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "bam dedup --recab"
refFile = " ~/Desktop/melanoma_RNASeq/indices/Homo_sapiens.GRCh38.dna.primary_assembly.fa"
input_dir = "--in ~/Desktop/melanoma_WES/Alignment/bwa_mem/sort/"
output_dir = "--out ~/Desktop/melanoma_WES/Alignment/bwa_mem/dedup_recab_combined/"
reads = " --oneChrom"
qualtiy_tag = " --storeQualTag OQ"
max_base_quality = " --maxBaseQual 40"

for x in accessions:
   
    command = inst_dir + refFile + input_dir + x + "_sorted.bam" + x + output_dir + x + ".bam" + " " + reads + qualtiy_tag + max_base_quality
    print(command + " ....running....")
    os.system(command)
    


print("All done")
