
def freq_list(x):
    res={}
    visited=[]

    for i in x:
        if i in visited:
            res[i]=res[i]+1
        else:
            res[i]=1
            visited+=[i]
    return res

x=[87,12,67,32,87,87,12,5,9,9,87]
print(freq_list(x))
