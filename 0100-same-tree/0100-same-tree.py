class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q: 
            if p.val != q.val:
                return False
            
            left = self.isSameTree(p.left, q.left) 
            right = self.isSameTree(p.right, q.right)
            return left and right
        
        if q == p:
            return True