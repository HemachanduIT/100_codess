# input1:
#     5
#     432 12 45 100 3
# output1:
#     2

# input2:
#     00 000
# output2:
#     1

def even_count(n,s):
    res=0
    # for i in range(n):
    #     if len(str(s[i]))%2==0:
    #         res+=1
    
    for i in s:
        if len(i)%2==0:
            res+=1
        
    return res
n=int(input())
# s=list(map(int,input().split()))
s=input().split()
print(even_count(n,s))