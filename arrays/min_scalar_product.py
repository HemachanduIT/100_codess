#scalar product(minimum)
# To minimize the scalar product, pair the largest elements of one vector with the smallest elements of the other.

# Because a big positive number × a big negative number makes a very negative product.

# This “opposite ordering” ensures the result is minimized.

# 1 2 6 3 7
# 10 7 45 3 7
# the minimum scalar product from arr1 and arr2 is 149


def minScalarProduct(arr1,arr2):
    arr1.sort()
    arr2.sort(reverse=True)
    # res=1
    s=0
    max_len=max(len(arr1),len(arr2))
    for i in range(max_len):
        res=arr1[i]*arr2[i]
        s+=res
    return s

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print("the minimum scalar product from arr1 and arr2 is",minScalarProduct(arr1,arr2))