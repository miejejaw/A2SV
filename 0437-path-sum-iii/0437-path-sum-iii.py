class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.helper(root,targetSum,0,{0:1})
        return self.ans
    
    def helper(self,curr,target,total,rem):
        if curr:
            total += curr.val
            if total - target in rem:
                self.ans += rem[total-target]
            
            temp = rem.get(total,0)+1
            self.helper(curr.left,target,total,rem|{total:temp})
            self.helper(curr.right,target,total,rem|{total:temp})
            