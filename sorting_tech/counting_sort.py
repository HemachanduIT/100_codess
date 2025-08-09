def count_sort(arr):
    n=len(arr)
    m=max(arr)
    count=[0]*(m+1)
    for i in arr:
        count[i]+=1
    i=0
    for c in range(m+1):
        while count[c]>0:
            arr[i]=c
            i+=1
            count[c]-=1
    return arr
a=[5,2,3,6,8,1,9]
print(count_sort(a))
            
        