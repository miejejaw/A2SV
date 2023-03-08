class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root,None,None)
        return self.ans
    
    def helper(self,curr,parent,grand):
        if curr:
            if grand and grand.val%2 == 0:
                self.ans += curr.val
            self.helper(curr.left,curr,parent)
            self.helper(curr.right,curr,parent)
        
                