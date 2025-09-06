#scalar product(maximum)
# To maximize the scalar product, pair the largest numbers of one vector with the largest numbers of the other vector.

# Similarly, the smallest (most negative) numbers should be paired with the smallest (most negative) numbers, so the product
# is positive and big.

# 10 30 40 20
# 2 4 5 1
# the maximum scalar product from arr1 and arr2 is 370

def sort(arr):
    flag=True
    while flag:
        flag=False
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                arr[i-1],arr[i]=arr[i],arr[i-1]
                flag=True
    return arr
                
def maxScalarProduct(arr1,arr2):
    a=sort(arr1)
    b=sort(arr2)
    max_len=max(len(a),len(b))
    s=0
    for i in range(max_len):
        res=a[i]*b[i]
        s+=res
    return s        
    
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print("the maximum scalar product from arr1 and arr2 is",maxScalarProduct(arr1,arr2))