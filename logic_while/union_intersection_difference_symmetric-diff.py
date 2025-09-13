# input:
# 1 2 3
# 2 3 4

# output:
# {1, 2, 3, 4}
# {2, 3}
# {1}
# {1, 4}



set1=list(map(int,input().split()))
set2=list(map(int,input().split()))
set_res=set1+set2
union=set()
d={}
for i in set1+set2:
    union.add(i)
for i in set_res:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
intersection={k for k,v in d.items() if v>1}
diff=set()
if len(set1)==len(set2):
    for i in range(len(set1)):
        diff.add(abs(set1[i]-set2[i]))
else:
    print("invalid sets")
symm_diff={k for k,v in d.items() if v==1}
print(union)
print(intersection)
print(diff)
print(symm_diff)
        
