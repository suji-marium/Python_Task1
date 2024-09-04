
def bsort(x):
    n=0
    for i in x:
        n=n+1

    for i in range(n):
        for j in range(0,n-i-1):
            if x[j]>x[j+1]:
                temp=x[j]
                x[j]=x[j+1]
                x[j+1]=temp

    print("Sorted list:",x)

x=[12,8,34,90,23,56]
bsort(x)