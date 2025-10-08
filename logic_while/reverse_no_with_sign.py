# input:
#     -123
# output:
#     -321

k=int(input())
r=0
n=abs(k)
sign=1 if k>0 else -1
while n!=0:
    r=r*10+n%10
    n//=10
r=r*sign
if r< -2**31 and r>2**31-1:
    print(0)
else:
    print(r)
