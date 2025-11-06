n=int(input())
s=list(str(n))
# print(s)
s[0],s[1]=s[1],s[0]
print(int(''.join(s)))