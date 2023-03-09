class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = -1
        self.smallest(root,k)
        return self.ans
    
    def smallest(self,curr,k):
        
        if curr and self.ans < 0:
            left = self.smallest(curr.left,k)
            if left == 1:
                self.ans = curr.val
                return left - 1
            
            right = self.smallest(curr.right,left-1)
            return right
            
        return k