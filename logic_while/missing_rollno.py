# input:
#     3
#     3 0 1
# output:
#     2

def missingNo(n,s):
    # m=max(s)
    for i in range(n+1):
        if i not in s:
            return i
n=int(input())
s=list(map(int,input().split()))
print(missingNo(n,s))