x=input("Enter the string:")
res=""
length=0
for i in x:
    length+=1

for i in range(length-1,-1,-1):
    res+=x[i]
print(res)