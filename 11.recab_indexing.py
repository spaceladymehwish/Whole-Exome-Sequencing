bamtools index -in samplename_recab.bam

eg. bamtools index -in SRR14753170_recab.bam

import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "bamtools index"
input_dir = "~/Desktop/melanoma_WES/Alignment/bwa_mem/dedup_recab_combined/"



for x in accessions:
   
    command = inst_dir + " -in " + input_dir + x + ".bam" 
    print(command)
    os.system(command)
    


print("All done")
