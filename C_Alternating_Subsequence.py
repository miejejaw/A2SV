t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    
    res = [nums[0]]
    flag = nums[0]>0
    for ind in range(1,n):
        if (nums[ind]>0 and flag) or (nums[ind]<0 and not flag):
            res[-1] = max(res[-1],nums[ind])
        elif (nums[ind]>0 and not flag) or (nums[ind]<0 and flag):
            res.append(nums[ind])
            flag = not flag
    print(sum(res))            
        