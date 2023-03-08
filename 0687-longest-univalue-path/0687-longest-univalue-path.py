class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root,None)
        return self.ans
    
    def helper(self,curr,parent):
        if curr:
            if not curr.left and not curr.right and parent:
                return 1 if curr.val == parent.val else 0
            
            left = self.helper(curr.left,curr)
            right = self.helper(curr.right,curr)
            self.ans = max(self.ans,left+right)
            if parent:
                return max(left,right) + 1 if parent.val == curr.val else 0
        return 0
