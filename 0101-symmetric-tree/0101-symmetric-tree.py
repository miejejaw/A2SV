class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(root.left,root.right)
    
    def helper(self,currLeft,currRight):
        if currLeft and currRight:
            if currLeft.val != currRight.val:
                return False
            left = self.helper(currLeft.left, currRight.right)
            right = self.helper(currLeft.right, currRight.left)
            return  left and right 
        
        if currLeft == currRight:
            return True
# 10