lst=[1,4,2,4,5,6,2,8,3,9,5]
temp=[]
for i in lst:
    if i not in temp:
        temp.append(i)
print("List without Duplicate Elements : ",temp)