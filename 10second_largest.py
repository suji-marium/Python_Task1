x=[12,8,34,90,23,56]

first_largest=x[0]
second_largest=x[0]

for i in x:
    if i>first_largest:
        first_largest=i

for i in x:
    if second_largest < i < first_largest:
        second_largest=i
#print(first_largest)
print("Second Largest element:",second_largest)