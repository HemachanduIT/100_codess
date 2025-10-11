# input:
#     4
#     1 3 5 6
#     7
# output:
#     4
    

n=int(input())
s=list(map(int,input().split()))
s.sort()
key=int(input())

for i in range(n):
    if s[i]>=key:
        print(i)
        break
else:
    print(n)
