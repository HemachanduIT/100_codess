s=list(map(int, input().split()))
summ=0
for i in range(len(s)):
    pos=sum(s[:i+1])
    summ=max(summ,pos)
print(summ)