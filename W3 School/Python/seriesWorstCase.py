sum = 0
n = int(input("n = "))

for i in range(1,n+1):
    for j in range(1,i+1):
        #print(j,end="+")
        sum = sum + j
    #print("  ",end="")
print("\n",sum,sep="")
