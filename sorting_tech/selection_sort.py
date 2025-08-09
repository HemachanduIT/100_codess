def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_ele=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ele]:
                min_ele=j
        arr[i],arr[min_ele]=arr[min_ele],arr[i]
    return arr
a=[5,4,7,2,1,8,9,-2,-6,-5]
print(selection_sort(a))