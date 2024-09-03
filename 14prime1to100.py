sum=0
for i in range(2,100):
    if i==2:
        print(i,end=' ')
        sum+=i
    else:
        flag=0
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i,end=' ')
            sum+=i
print("\nSum:",sum)
