# 2 3 6 1 5 9
# the result sort is 1 2 3 9 6 5


s=list(map(int,input().split()))
s.sort()
a=s
i=a
# print(i)
r=i[:len(s)//2]
a.sort(reverse=True)
b=a
# print(b)
c=r+b[:len(s)//2]
print("the result sort is",*c)