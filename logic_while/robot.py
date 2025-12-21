# input:
#     G()(al)
# output:
#     GoStopTurn

s=input()
res=''
for i in range(len(s)):
    if s[i]=='G':
        res+='Go'
    elif s[i]=='(' and s[i+1]==')':
        res+='Stop'
    elif s[i]=='[' and s[i+1]=='A' and s[i+2]=='L' and s[i+3]==']':
        res+="Turn"
print(res)
        