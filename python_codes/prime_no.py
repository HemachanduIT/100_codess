n=int(input())
c=0
# if n==2:
#     c=1

# for i in range(3,int(pow(n,0.5)),2):
#     if n%i==0:
#         c=1
        # break
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(n,'is a prime no')
else:
    print(n,'is not a prime no')
    