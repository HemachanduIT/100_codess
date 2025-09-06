# 1 2 3 4 5 6 7
# the even count is 3
# the odd count is 4

def even_odd_count(s):
    e_c,o_c=0,0
    for i in s:
        if i%2==0:
            e_c+=1
        else:
            o_c+=1
    return e_c,o_c

s=list(map(int,input().split()))
even_count,odd_count=even_odd_count(s)
print("the even count is",even_count)
print("the odd count is",odd_count)