elt=[99,7,16,5,38,8,0]

large=elt[0]
for i in elt:
    if i>large:
        large=i

print("Largest element in the list:",large)