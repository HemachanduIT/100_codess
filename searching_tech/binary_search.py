string=list(map(int,input().split()))
k=int(input())

def binary_search(s,k):
    l,h=0,len(s)-1
    f=0
    while l<h:
        m=(l+h)//2
        if s[m]==k:
            print("element"+k+"found")
            f=1
            break
        elif s[m]>k:
            h=m-1
        else:
            l=m+1

    if f==0:    
        print("element ",k," not found")
binary_search(string,k)
