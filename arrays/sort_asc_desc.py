# 2 3 4 1 0
# the sorting in descending orderis 4 3 2 1 0

# 2 3 4 1 0
# the sorting in ascending orderis 0 1 2 3 4

n=list(map(int,input().split()))
n.sort()
# n.sort(reverse=True)
print("the sorting in ascending orderis",*n)
# print("the sorting in descending orderis",*n)