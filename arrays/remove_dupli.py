# 10 20 20 30 40 40 40 50 50
# the array after removing duplicate elements are: 10 20 30 40 50


def removeDuplicate(s):
    res=[]
    for i in s:
        if i not in res:
            res.append(i)
    return ' '.join(map(str,res))
    
    # if len(s)==0 or len(s)==1:
    #     return ' '.join(map(str,s))
    # j=0
    # for i in range(0,len(s)-1):
    #     if s[i]!=s[i+1]:                   #s[j]=10,20,30,40,
    #         s[j]=s[i]
    #         j+=1
    # s[j]=s[len(s)-1]
    # # j+=1
    # return s[j]            
s=list(map(int,input().split()))
print("the array after removing duplicate elements are:",removeDuplicate(s))