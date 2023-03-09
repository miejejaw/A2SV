class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.num = float("inf")
        self.isValid(root,False)
        return self.ans
    
    def isValid(self,curr,parent):
        if curr and self.ans:
            
            self.isValid(curr.right,False)
            if self.num <= curr.val:
                self.ans = False
                return
            self.num = curr.val
            self.isValid(curr.left,True)
            