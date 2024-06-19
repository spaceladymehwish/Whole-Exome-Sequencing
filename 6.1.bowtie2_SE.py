
import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "bowtie2"
indices = "/home/bushra/Desktop/homosapiens"
option_SE = "-U"
input_dir = "/home/bushra/Desktop/trimmed/"
output_sam_dir = "/home/bushra/Desktop/sam/"
output_sorted_sam = "/home/bushra/Desktop/sorted_sam/"
output_bam = "/home/bushra/Desktop/bam/"
output_sum = "/home/bushra/Desktop/summary/"
output_unaligned = "/home/bushra/Desktop/nonaligned/"

cores = " -p 6"


for x in accessions:
   
    command = inst_dir + cores + " -x " + indices  + " -U "  + input_dir + x + "_trimmed.fastqsanger.gz" + " -S " + output_sam_dir + x + ".sam" + " --un " + output_unaligned + x + "_nonaligned.sam" + " -s "+ output_sum + x + "_summary.txt"
    print(command + " ....running....")
    os.system(command)
    command = "samtools sort" + " " + output_sam_dir + x + ".sam" + " -o " + output_sorted_sam + x + "_sorted.sam " 
    print(command)
    os.system(command)
    command = "samtools view" + " -bS " + output_sorted_sam + x + "_sorted.sam" " > " + output_bam + x + ".bam"
    print(command)
    os.system(command)

print("All done")
