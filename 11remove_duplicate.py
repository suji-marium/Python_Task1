x=[2,9,11,6,9,11,8]

unique=[]
for i in x:
    if i not in unique:
        unique+=[i]
print(unique)