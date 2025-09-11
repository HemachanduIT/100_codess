# hello hello chandu
# {'hello': 2, 'chandu': 1}
from collections import Counter
def wordCounter(s):
    # d=dict()
    # for i in s:
    #     if i in d:
    #         d[i]+=1
    #     else:
    #         d[i]=1
    d=Counter(s)
    return d
s=list(map(str,input().split()))
print(wordCounter(s))