def merge_sort(arr):
    n=len(arr)
    if n==1:
        return arr
    m=len(arr)//2
    L=arr[:m]
    R=arr[m:]
    L=merge_sort(L)
    R=merge_sort(R)
    l,r=0,0
    sor_arr=[0]*n
    L_len=len(L)
    R_len=len(R)
    i=0
    while l<L_len and r<R_len:
        if L[l]<R[r]:
            sor_arr[i]=L[l]
            l+=1
        else:
            sor_arr[i]=R[r]
            r+=1
        i+=1
    while l<L_len:
        sor_arr[i]=L[l]
        l,i=l+1,i+1
    while r<R_len:
        sor_arr[i]=R[r]
        r,i=r+1,i+1
    return sor_arr
arr=[5,4,7,2,1,8,9,-2,-6,-5]
print(merge_sort(arr))
            