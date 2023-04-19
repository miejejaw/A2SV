class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        self.dfs(root)
        return self.ans
    
    def dfs(self, curr):
        if curr:
            left = self.dfs(curr.left)
            right = self.dfs(curr.right)
            
            if left < 0:
                left = 0
            if right < 0:
                right = 0
                
            self.ans = max(self.ans,curr.val+left+right)
            return curr.val + max(left,right) 
        
        return 0