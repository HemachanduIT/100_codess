def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    p=arr[-1]
    l=[x for x in arr[:-1] if x<=p]
    r=[x for x in arr[:-1] if x>p]
    l=quick_sort(l)
    r=quick_sort(r)
    return l+[p]+r
a=[5,4,7,2,1,8,9,-2,-6,-5]
print(quick_sort(a))