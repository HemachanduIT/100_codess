# apple banana cherry date fig grape
# {5: ['apple', 'grape'], 6: ['banana', 'cherry'], 4: ['date'], 3: ['fig']}

def group_words_by_len(s):
    d={}
    res={}
    for i in s:
        d[i]=len(i)
    for k,v in d.items():
        if v in res:
            res[v].append(k)
        else:
            res[v]=[k]
    return res

s=list(map(str,input().split()))
print(group_words_by_len(s))