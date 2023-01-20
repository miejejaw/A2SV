testcase = int(input())
for _ in range(testcase):
    size = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    res = "YES"
    for ind in range(1,size):
        if nums[ind]-nums[ind-1]>1:
            res = "NO"
            break
    print(res)
    