import os


file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()



command = "cutadapt in1.fastq in2.fastq -o out1.fastq -p out2.fastq"

inst_dir = "cutadapt"
input_dir = "/home/bushra/Desktop/LungCarcinoma/inputdata/"
output_dir = "/home/bushra/Desktop/LungCarcinoma/trimmed/"

for x in accessions:
   
    command = inst_dir + " " + "-j 6" + " " + "-a AGATCGGAAGAG" + " " + "-A AGATCGGAAGAG" + " " + input_dir + x + "_1.fastq.gz" + " " + input_dir + x + "_2.fastq.gz" + " -o " + output_dir + x + "_1_trimmed.fastq.gz" + " -p " + output_dir + x + "_2_trimmed.fastq.gz"
    print(command + " ....running....")
    os.system(command)

print("All done")
