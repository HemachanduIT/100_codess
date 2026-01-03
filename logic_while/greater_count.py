# input:
#     6
#     88 45 67 67 72 80
# output:
#     5 0 1 1 3 4

def greatercount(n,s):
    res=[]
    for i in range(n):
        c=0
        maxx=s[i]
        for j in range(n):
            # maxx=s[i]
            if maxx>s[j]:
                c+=1
        res.append(c)
    return ' '.join(map(str,res))
no=int(input())
ss=list(map(int,input().split()))
print(greatercount(no,ss))