import math
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    k=i
    s=0
    c=(int)(math.log10(i)+1)
    while i!=0:
        s+=math.pow(i%10,c)
        i//=10
    if s==k:
        print(k,"is armstrong")
    # else:
    #     print(k,"not armstrong")
    
    