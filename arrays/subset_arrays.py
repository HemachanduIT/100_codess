# 1 2 3 4 4 5
# 2 3 5
# arr2 is subset of arr1


def subarray(arr1,arr2):
    for i in arr2:
        if i in arr1:
            continue
        else:
            return False
    return True

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
if subarray(arr1,arr2):
    print("arr2 is subset of arr1")
else:
    print("arr2 is not subset of arr1")