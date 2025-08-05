l1=[21,23,44,14,87,53]
highest=l1[0]
for i in range(0,len(l1)-1): 
    if highest<l1[i]:
        highest=l1[i]
print(highest)


second=l1[0]
for i in range(len(l1)):
    if l1[i]>second and highest>l1[i]:
        second=l1[i]

print(second)







    



