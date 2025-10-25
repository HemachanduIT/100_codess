# input:
#     abcde
#     ghij
# output:
#     agbhcidje

def concate(s1,s2):
    res=''
    minn=min(len(s1),len(s2))
    for i in range(minn):
        res+=s1[i]+s2[i]
    if len(s1)>len(s2):
        a=s1
    else:
        a=s2
    res+=a[minn:]
    return res
s1=input()
s2=input()
print(concate(s1,s2))