x=input("Enter the string: ")
length=0
for i in x:
    length+=1

print(length)
flag=0
for i in range (0, length):
    if x[i]!=x[length - i - 1]:
        flag=1
        break

if flag==0:
    print(x, "is palindrome")
else:
    print(x, "is not palindrome")