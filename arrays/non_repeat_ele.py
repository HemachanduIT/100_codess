# 10 20 70 90 80 20 10 20
# the non-repeating elements are: 70 90 80

def nonRepeat(s):
    d=dict()
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    res=[k for k,v in d.items() if v==1]
    return ' '.join(map(str,res))
s=list(map(int,input().split()))
print("the non-repeating elements are:",nonRepeat(s))