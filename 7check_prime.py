
def check_prime(num):
    flag=0
    if num==1:
        print(num, "is neither prime or composite")
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True


num=int(input("Enter a number: "))
if check_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")