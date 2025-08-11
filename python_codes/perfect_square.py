import math
n=int(input())
def is_perfect_square(n):
    if n>0:
        
     s=int(math.sqrt(n))
     return n==s*s
    return False
if is_perfect_square(n):
    print("perfect square")
else:
    print("not a perfect square")
    