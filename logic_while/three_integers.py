# input:
#     12345 78 9876 
# output: 
#     38087

a,b,c=map(str,input().split())
n1=''
n2=''
n3=''
#1st condition
le=len(a)//2
if len(a)%2==0:
    n1=a[le-1]+a[le]
else:
    n1=a[le]
# print(n1)

#2nd condition
if len(b)<3:
    n2=b[-1]+'0'
else:
    n2=b[1]+b[2]
# print(n2)

#3rd condition
if len(c)==1:
    n3=c[0]+'0'
else:
    n3=c[-3]+c[-2]
# print(n3)
print(int(n1+n2+n3))



        
    