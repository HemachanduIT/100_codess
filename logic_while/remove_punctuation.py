# input:
#     Logicwhile provides quality training.logicwhile helps students
# output:c
    # ['provides', 'quality', 'training', 'helps', 'students']
import string
def sentenceremoval(s):
    for i in string.punctuation:
        s=s.replace(i," ")
    s=s.lower()
    w=s.split()
    d={}
    for i in w:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    res=[k for k,v in d.items() if v==1]
    return res
            
s=input()
print(sentenceremoval(s))
# print(s)
