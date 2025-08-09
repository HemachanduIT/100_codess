def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break
    return arr
a=[5,4,7,2,1,8,9,-2,-6,-5]
print(insertion_sort(a))