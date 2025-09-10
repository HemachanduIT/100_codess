# 3
# Logic While Hyderabad
# ['oi', 'ie', 'eaa']


def vowelsidentify(n,s):
    v=['a','e','i','o','u','A','E','I','O','U']
    res=[]
    # a=''
    for i in s:
        a=''
        for char in i:
            if char in v:
                a+=char
        res.append(a)
    return res
            

n=int(input())
s=list(map(str,input().split()))
print(vowelsidentify(n,s))