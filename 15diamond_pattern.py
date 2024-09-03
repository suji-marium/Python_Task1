"""
n=int(input("Enter a number:"))
j=0
for i in range(1,n+1):

    j=1
    while j<=i:
        j=j+1
        print("*",end='')
    print("\n")
"""

n=int(input("Enter the number of rows: "))

for i in range(0,n):
    for j in range(0, n - i - 1):
        print(" ", end='')
    for j in range(0, i + 1):
        print("* ", end='')
    print()

for i in range(0,n-1):
    for j in range(0,i+1):
        print(" ",end='')
    for j in range(0,n-i-1):
        print("* ",end='')
    print()

