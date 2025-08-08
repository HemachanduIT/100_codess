s=list(map(int,input().split()))
k=int(input())
def linear_search(s,k):
    for i in s:
        if i==k:
            print(k,"element found")
            break
    else:
        print(k,"element not found")

linear_search(s,k)