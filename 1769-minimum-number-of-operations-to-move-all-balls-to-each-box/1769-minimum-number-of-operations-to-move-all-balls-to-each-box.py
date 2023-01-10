class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        ones = 0
        total = 0
        for i,num in enumerate(boxes):
            ans[i] = total + ones
            total += ones
            if num=='1':
                ones += 1
        ones = 0
        total = 0
        for i in range(len(ans)-1,-1,-1):
            ans[i] += total + ones
            total += ones
            if boxes[i]=='1':
                ones += 1
        return ans
            
            
                
                    
                    
        