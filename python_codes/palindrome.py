n=int(input())
r=int(str(n)[::-1])
# k=n
# r=0
# while n!=0:
#     r=r*10+n%10
#     n//=10
if n==r:
    print("palindrome")
else:
    print("not a palindrome")
# print("palindrome") if (n==str(n)[::-1]) else print("not a palindrome")