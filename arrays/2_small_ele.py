# 1 2 3 -1 0
# the 2nd smallest no is 0

s=list(map(int,input().split()))
flag=True
while flag:
    flag=False
    for i in range(1,len(s)):
        if s[i]<s[i-1]:
            s[i],s[i-1]=s[i-1],s[i]
            flag=True
            break
print("the 2nd smallest no is",s[1])
            
    
# s.sort()
