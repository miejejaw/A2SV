class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = []
        self.isValid(root,None,None)
        for ind in range(1,len(self.ans)):
            if self.ans[ind]<=self.ans[ind-1]:
                return False
        return True
    
    def isValid(self,curr,parent,grand):
        if curr :
            
            self.isValid(curr.left,curr,parent)
            self.ans.append(curr.val)
            self.isValid(curr.right,curr,grand)
            