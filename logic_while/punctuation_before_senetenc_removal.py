import string
def sentenceremoval(s):
    output=[]
    flag=True
    for word in s:
        res=''
        res1=''
        for char in word:
            if char not in string.punctuation:
                if flag:
                    res+=char
                res1+=char
            elif char in string.punctuation:
                flag=False
                continue
        output.append(res)
        # output.append(res1)
        print(res1)
        
    return output

            
s=input().split()
print(sentenceremoval(s))
# print(s)
