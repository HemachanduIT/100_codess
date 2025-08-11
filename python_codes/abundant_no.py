n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
print("abundant no") if s>n else print("not an abundant")    