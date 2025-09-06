# 10,20,40,30,50,20,10,20
# the distinct elements count is 5

def distinct_ele(s):
    res=[]
    for i in s:
        if i not in res:
            res.append(i)
    return len(res)
    
s=list(map(int,input().split(",")))
print("the distinct elements count is",distinct_ele(s))