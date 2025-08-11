# a,b=0,1 
# print(a,b, end=' ')
k=int(input())
a,b=0,1
s=0
n=[0,1]
for i in range(2,11):
    s=a+b
    n.append(s)
    a=b 
    b=s
print("the",k,"th position fib value is",n[k])
