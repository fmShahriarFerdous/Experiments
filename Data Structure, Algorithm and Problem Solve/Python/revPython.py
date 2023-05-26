def findGCD (a,b):
    if(a%b==0):
        GCD = b
        return GCD
    else:
        return findGCD(b,(a%b))

def findLCM(a,b,GCD):
    return a*b/GCD

a = int(input("Enter a number "))
b = int(input("Enter a number "))
GCD = findGCD(a,b)
LCM = int(findLCM(a,b,GCD))
print("GCD is",GCD)
print("LCM is",LCM)