# input:
#     Mango
# output:
#     MMnnggaaaaao
import string
s=input()
v=['a','e','i','o','u','A','E','I','O','U']
all=list(string.ascii_letters)
conso=list(set(all)-set(v))
result=''
conso_res=''
vowel_res=''

for i in range(len(s)):
    
    if s[i] in conso:
        conso_res+=s[i]*2
    elif s[i] in v:
        c=0
        if i!=len(s)-1:
            for j in range(i+1,len(s)):
                
                if s[j] in v:
                    c=j+1
                    # print(c)
                    break
            vowel_res+=s[i]*c
        else:
            vowel_res+=s[i]
result=conso_res+vowel_res
print(result)
    # elif s[i] in v:
        
        
