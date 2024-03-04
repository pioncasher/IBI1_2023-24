# initial density is 0.05
# Repeat 
#   The cell culture density larger than 0.9?
#   No, cell density doubles
#   Yes, exit the loop
# print the result

init=0.05
d=0
while init<=0.9:
    init*=2
    d+=1
print("Cell culture density exceeds 90% on the "+str(d)+"th day.")

