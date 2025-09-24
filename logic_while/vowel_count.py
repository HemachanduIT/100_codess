# input:
#     Time Travel Book
# output:
#     Time : 2  
#     Travel : 2
#     Book : 2

s=list(map(str,input().split()))
v=['a','e','i','o','u','A','E','I','O','U']
for word in s:
    c=0
    for char in word:
        if char in v:
            c+=1
    print(word,":",c)
    
    
    
