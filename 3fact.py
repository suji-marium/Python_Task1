
def factorial(x):
    fact=1

    for i in range(1,x+1):
        fact=fact*i
    return fact

x=int(input("Enter the number: "))
print("Factorial of",x, "is",factorial(x))
