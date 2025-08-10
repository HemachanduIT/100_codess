n=int(input())
s=0
# while n!=0:
#     s+=n%10
#     n//=10
for i in str(n):
    s+=int(i)
print(s)