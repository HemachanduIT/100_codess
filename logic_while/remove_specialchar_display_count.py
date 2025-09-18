# input:
#     Logicwhile provides training.Logicwhile helps students succedd!
# output:
    # Logicwhile:2
    # provides:1
    # training:1
    # helps:1
    # students:1
    # succedd:1

import string
s=input()
for i in string.punctuation:
    s=s.replace(i," ")
w=s.split()
d={}
for i in w:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    print(f"{k}:{v}")