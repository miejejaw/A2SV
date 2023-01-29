n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
res = -1

if (0<k<n and arr[k]!=arr[k-1]) or k==n:
    res = arr[k-1]
elif k==0 and arr[k]>1:
    res = arr[k]-1
    
print(res)