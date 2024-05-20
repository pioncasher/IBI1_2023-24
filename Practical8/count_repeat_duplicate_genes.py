import re
rep_seq=input("Please choose the input repetitive sequence,you can input GTGTGT or GTCTGT")
output = f"{rep_seq}_duplicate_genes.fa"       
with open('duplicate_genes_.fa', 'r') as fasta:     
    lines = fasta.readlines()

with open(output, 'w') as out:        
    gene = False            
    gene_name = None
    gene_seq = ""        

    for line in lines:
        if line.startswith(">"):
            if gene and gene_name:  
                repeat_count = gene_seq.count(rep_seq)      
                out.write(f">{gene_name} \n")    
                out.write(f"{repeat_count}  {gene_seq} \n")
            gene = True         
            gene_name = line.strip()[1:].split(' ')[0]    
            gene_seq = ""
        else:
            if gene:                  
                gene_seq += line.strip()       
