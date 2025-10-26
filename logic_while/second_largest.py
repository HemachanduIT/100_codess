s=list(map(int,input().split()))
if len(s)==1:
    print("no second largest ")
else:
    s.sort()
    print(s[-2])