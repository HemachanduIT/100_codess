# input:
#     laddu jalebi barfi    
# output:  
#     ['ladu', 'jalebi', 'barfi']
s=list(map(str,input().split()))
res=[]
for i in s:
    var=''
    for char in i:
        if char not in var:
            var+=char
    res.append(var)
print(res)     
        