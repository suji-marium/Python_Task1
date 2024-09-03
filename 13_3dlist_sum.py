x=[
    [
        [3,2,5],
        [2,8]
    ],
    [
        [11,9,7],
        [8,4]
    ],
    [
        [45,87],
        [32,19]
    ]
]

for i in x:
    print(i)
    for j in i:
        print(j)
        sum=0
        for k in j:
            sum+=k
        print("Sum of" ,j, ":",sum)


