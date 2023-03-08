class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.helper(root.left,root.right)
        return self.ans
    
    def helper(self,l,r):
        if self.ans and l and r:
            if l.val != r.val:
                self.ans = False
            self.helper(l.left, r.right)
            self.helper(l.right, r.left)
            return   
        
        if l != r:
            self.ans = False
# 10