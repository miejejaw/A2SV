class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.helper(root)
        return self.ans
    
    def helper(self,curr):
        if self.ans and curr:
            left = self.helper(curr.left)
            right = self.helper(curr.right)

            if abs(right-left) > 1:
                self.ans = False

            return max(right,left)+1
        return 0