import string
def sentenceremoval(s):
    output=[]
    
    for word in s:
        res=''
        for char in word:
            if char not in string.punctuation:
                res+=char
            elif char in string.punctuation:
                res
        output.append(res)
        
    return output
            
s=input().split()
print(sentenceremoval(s))
# print(s)