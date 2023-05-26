n = 3
if(n>0):
    sum =0
    for i in range(2,n+1):
        sum = sum + i
    print(sum)
else:
    sum = 0
    for i in range(n,-1):
        sum = sum + i
    print(sum)

