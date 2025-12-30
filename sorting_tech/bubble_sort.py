def bubble_sort(arr):
    n=len(arr)
    f=True
    while f:
        f=False
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                arr[i-1],arr[i]=arr[i],arr[i-1]
                f=True
    return arr
    
arr=[5,4,7,2,1,8,9,-2,-6,-5]
print(bubble_sort(arr))