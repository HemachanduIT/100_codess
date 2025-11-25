def sum_of_ids(n,s):
    result=[]
    # for i in range(n):
    #     a=s[i]
    #     summ=0
    #     while a!=0:
    #         r=a%10
    #         summ+=r
    #         a//=10
    #     res.append(summ)
    
    for i in s:
        summ=0
        for j in str(i):
            summ+=int(j)
        result.append(summ)
    return ' '.join(map(str,result))
n=int(input())
s=list(map(int,input().split()))
print(sum_of_ids(n,s))