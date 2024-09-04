

def largest(elt):
    large=elt[0]
    for i in elt:
        if i>large:
            large=i
    return large

elt=[99,7,16,5,38,8,0]
print("Largest element in the list:",largest(elt))