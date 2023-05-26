num = [6,5,4,3,2,1]
n = 6
for i in range (0,n):
    print("i = ",i)
    for j in range(0,n-1):
        print("compare between",num[j],"and",[num[j+1]])
        if(num[j+1] < num[j]):
            print("swapping........")
            num[j+1],num[j]=num[j],num[j+1]
            print(num)
        else:
            print("skip")
        print("\n")
        