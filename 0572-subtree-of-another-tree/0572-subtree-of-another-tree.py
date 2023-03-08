class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        self.helper(root,subRoot)
        return self.ans
    
    def helper(self,curr,subRoot):
        if not self.ans and curr:
            self.ans = self.isSubTree(curr,subRoot)
            self.helper(curr.left, subRoot)
            self.helper(curr.right, subRoot)
            return
        return
            
    def isSubTree(self,curr,subRoot)->bool:
        if curr and subRoot:
            if curr.val != subRoot.val:
                return False
            left = self.isSubTree(curr.left, subRoot.left)
            right = self.isSubTree(curr.right, subRoot.right)
            
            return left and right
        
        if not curr and not subRoot:
            return True
        return False