num = [5,2,6,1,4,3]
n = 6
for i in range (0,n):
    for j in range(i+1,n):
        if(num[i] > num[j]):
            print("compare between",num[i],"and",[num[j]])
            num[i],num[j]=num[j],num[i]
            print(num)
    print("\n\n")
#print(num)

