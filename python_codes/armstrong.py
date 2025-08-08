import math
n=int(input())
k=n
c=(int)(math.log10(n)+1)
# print(c)
s=0
while n!=0:
    s+=math.pow(n%10,c)
    n//=10
if k==s:
    print("armstrong")
else:
    print("not an armstrong")
    