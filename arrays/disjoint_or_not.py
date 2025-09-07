# 1 2 3 4 5
# 4 5 6 7 8
# the arrays are  not disjoint

# 1 2 3 4 5
# 6 7 8 9 10
# the arrays are  disjoint

def isDisjointornot(arr1,arr2):
    c=0
    for i in arr1:
        if i in arr2:
            c+=1
    if c>=1:
        return "not disjoint"
    else:
        return "disjoint"

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print("the arrays are ",isDisjointornot(arr1,arr2))