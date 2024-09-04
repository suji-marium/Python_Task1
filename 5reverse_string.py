
def reverse_string(x):
    res=""
    length=0
    for i in x:
        length+=1

    for i in range(length-1,-1,-1):
        res+=x[i]
    return res

x=input("Enter the string:")
print("Reverse of the string is:",reverse_string(x))