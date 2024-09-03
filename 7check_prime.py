num=int(input("Enter a number: "))
flag=0
if num==1:
    print(num, "is neither prime or composite")
for i in range(2,num//2+1):
    if num%i==0:
        flag=1
        break
if flag==1:
    print(num,"is not a prime number")
else:
    print(num, "is a prime number")
