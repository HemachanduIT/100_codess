def bubble_sort(arr):
    n=len(arr)
    flag=True
    while flag:
        flag=False
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                arr[i-1],arr[i]=arr[i],arr[i-1]
                flag=True
    return arr
    
a=[5,4,7,2,1,8,9,-2,-6,-5]
print(bubble_sort(a))