class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        length = len(nums)
        if length == 1 and nums[0] == k:
            return 1
        nums = [0]+list(accumulate(nums))
        que = deque()
        ans = length+1
        for end,num in enumerate(nums):
            
            while que and que[-1][0] >= num:
                que.pop()
            que.append((num,end))
            
            while que[0][1]<que[-1][1] and que[-1][0]-que[0][0] >= k:
                ans = min(ans,que[-1][1]-que[0][1])
                que.popleft()
            
        return ans if ans<=length else -1