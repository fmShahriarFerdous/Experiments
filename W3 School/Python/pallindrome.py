def pallindrome(st,end,str):
    if(st > end ):
        return 1
    if(str[st] == str[end]):
        return pallindrome(st+1,end-1,str)
    else:
        return 0

    

str = "abgtgba"
#print(str)
end = len(str)
if(pallindrome(0,end-1,str)):
    print("Pallindrome")
else:
    print("Not Pallindrome")
