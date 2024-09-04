
def palindrome(x):

    length=0
    for i in x:
        length+=1

    flag=0
    for i in range (0, length):
        if x[i]!=x[length - i - 1]:
            return False
    return True

word=input("Enter the string: ")
if palindrome(word):
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")