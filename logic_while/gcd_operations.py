# input:
#     15 9
# output:
    # 2
    
def noofoperations(n1,n2):
    c=0
    # div
    while n1>0 and n2>0:
        div=gcd(n1,n2)
        n1-=div
        n2-=div
        c+=1
    return c
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n1,n2=map(int,input().split())
print(noofoperations(n1,n2))