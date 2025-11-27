# input:
#     7 50
# output:
#     1 12 5 111 200 1000 10

def maxtoys(n,k,prices):
    prices.sort()
    sum_res=0
    c=0
    for i in prices:
        if i<=k and sum_res<=k:
            sum_res+=i
            c+=1
    return c
n,k=map(int,input().split())
p=list(map(int,input().split()))
print(maxtoys(n,k,p))