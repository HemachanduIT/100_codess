# input:
#     4
# output:
#     1 1 1 1
#     2 2 2 10
#     3 3 3 11
#     4 4 4 100

n=int(input())
for i in range(1,n+1):
    decc=i
    octal=oct(i)
    hexa=hex(i)
    binary=bin(i)
    print(decc,octal[2:],hexa[2:],binary[2:])
