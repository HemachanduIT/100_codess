# 5
#         1 
#       2 2
#     3 3 3
#   4 4 4 4
# 5 5 5 5 5




n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    a=1
    for j in range(i+1):
        # a=1
        print(i+a,end=" ")
        a-=1
    print()
    
# 5
#         1 
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1