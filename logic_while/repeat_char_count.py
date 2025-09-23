# input:
#     logic
# output:
#     loogggiiiiccccc

def counter(s):
    res=''
    for i in range(len(s)):
        res+=s[i]*(i+1)
    return res
s=input()
print(counter(s))
