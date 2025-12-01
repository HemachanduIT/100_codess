# input:
#     Time Travel Book
# output:
#     Time : 2  
#     Travel : 2
#     Book : 2

string=list(map(str,input().split()))
v=['a','e','i','o','u','A','E','I','O','U']
for word in string:
    c=0
    for char in word:
        if char in v:
            c+=1
    print(word,":",c)
    
    
    
