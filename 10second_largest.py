
def second_large(x):
    first_largest=x[0]
    second_largest=x[0]

    for i in x:
        if i>first_largest:
            first_largest=i

    for i in x:
        if second_largest < i < first_largest:
            second_largest=i
    return second_largest

x=[12,8,34,90,23,56]
print("Second Largest element:",second_large(x))