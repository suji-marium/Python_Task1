
def common_elmt(x,y):
    for i in x:
        if i in y:
            print(i,end=' ')

x=[21,78,56,89,12,56,7]
y=[9,89,25,67,12,90,125,299,21]
common_elmt(x,y)