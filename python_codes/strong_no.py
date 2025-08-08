n=int(input())
k=n
s,r=0,0
while n!=0:
    f=1
    r=n%10
    for i in range(1,r+1):
        f=f*i
    s+=f
    n//=10
if s==k:
    print("strong no")
else:
    print("not a strong no")
    
    