import blosum
bl=blosum.BLOSUM(62) 

human=open("SLC6A4_HUMAN.fa",'r')
mouse=open("SLC6A4_MOUSE.fa",'r')
rat=open("SLC6A4_RAT.fa",'r')

def extract_seq(seq_file):
    seq=""
    for line in seq_file:
        if line[0] != ">":
           seq= seq+line[0:-1]
    return seq

human_seq=extract_seq(human)
mouse_seq=extract_seq(mouse)
rat_seq=extract_seq(rat)

def seq_align(seq1,seq2):
    score=0
    for i in range(len(seq1)):
        if seq1[i]==seq2[i]:
           score+=bl[seq1[i]][seq2[i]]
        else:
            score+=bl[seq1[i]][seq2[i]]
    return score

def ident_percentage(seq1,seq2):
    hamming_distance=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            hamming_distance+=1
    percentage=(((len(seq1))-hamming_distance)/len(seq1))*100
    return percentage



print('Alignment score of human and rat: '+str(seq_align(human_seq,rat_seq)))
print('Alignment score of human and mouse: '+str(seq_align(human_seq,mouse_seq)))
print('Alignment score of rat and mouse: '+str(seq_align(rat_seq,mouse_seq)))
        
print('Percentage of identical ammino acids between human and rat: '+str(ident_percentage(human_seq,rat_seq))+'%')
print('Percentage of identical ammino acids between human and mouse: '+str(ident_percentage(human_seq,mouse_seq))+'%')
print('Percentage of identical ammino acids between rat and mouse: '+str(ident_percentage(mouse_seq,rat_seq))+'%')

# output
# Alignment score of human and rat: 3107.0
# Alignment score of human and mouse: 3137.0
# Alignment score of rat and mouse: 3261.0
# Percentage of identical ammino acids between human and rat: 91.74603174603175%
# Percentage of identical ammino acids between human and mouse: 92.53968253968254%
# Percentage of identical ammino acids between rat and mouse: 96.82539682539682%


# Summary

# Sequence of rat and mouse is the most closely related 
# Mouse is a better model organism for human based on the data analysed here.

            