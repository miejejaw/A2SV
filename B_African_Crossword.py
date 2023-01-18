n,m = map(int,input().split())
arr,res = [],[]
for _ in range(n):
    arr.append(input())
    
for row in range(n):
    for col in range(m):
        temp = arr[row].count(arr[row][col])
        if temp>1:
            continue
        count = 0
        
        for ind in range(n):
            if arr[ind][col]==arr[row][col]:
                count += 1
                
        if count==1:
            res.append(arr[row][col])

print("".join(res))       