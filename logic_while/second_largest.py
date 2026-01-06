ss=list(map(int,input().split()))
if len(ss)==1:
    print("no second largest ")
else:
    ss.sort()
    print(ss[-2])