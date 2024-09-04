
def remove_duplicate(x):
    unique=[]
    for i in x:
        if i not in unique:
            unique+=[i]
    return unique
x=[2,9,11,6,9,11,8]
print(remove_duplicate(x))