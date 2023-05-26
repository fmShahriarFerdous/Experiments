# def isPalindrome(x):
#     num1 = x
#     rev = 0
#     while(num1 != 0):
#         rem = num1 % 10
#         num1 = int(num1 / 10)
#         rev = rev*10 + rem
#     if(x == rev):
#         return True
#     else:
#         return False
    
# x = -121
# b = isPalindrome(x)
# print(b)

def isPallindrome(x):
    strr = str(x)
    st = 0
    end = len(strr)
    b = pallindrome(st,end-1,strr)
    if b == 1:
        return True
    else:
        return False
    

def pallindrome(st,end,str):
    if(st > end ):
        return 1
    if(str[st] == str[end]):
        return pallindrome(st+1,end-1,str)
    else:
        return 0  

num = -121
print(isPallindrome(num))

