fasta=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
fout=open("duplicate_genes.fa","w")
dup_flag = False  
import re
a=''
for line in fasta:
    if line.startswith(">"):
       if line.find("duplication")>=0:
            gene_name=(re.findall(r'>[0-9a-zA-Z\_]*',line)[0])
            fout.write(gene_name+"\n")
            dup_flag=True
       else:
            dup_flag = False      
    
    elif dup_flag:      
        fout.write(line)  