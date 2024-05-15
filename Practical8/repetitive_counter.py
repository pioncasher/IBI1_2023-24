seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

count_1=0
count_2=0
for i in range(len(seq)-5):
        if seq[i:i+6]=="GTGTGT":
            count_1+=1
        elif  seq[i:i+6]=="GTCTGT":
            count_2+=1
        else:
             continue
total_count=count_1+count_2
print('The counts of \"GTGTGT\" is '+ str(count_1))
print('The counts of \"GTCTGT\" is '+ str(count_2))
print("Total count is "+ str(total_count))