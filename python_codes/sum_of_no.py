n=int(input())
# s=(n*(n+1))//2
s=0
for i in range(1,n+1):
    s+=i
print(s)