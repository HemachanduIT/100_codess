# A2b3c2@2
# AAbbbcc@@

def concate(s):
    res=''
    for i in range(0,len(s)-1,2):
        res+=(s[i])*(int(s[i+1]))
    return res
s=input()
print(concate(s))