class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.ans = True
        self.trav(p, q)
        return self.ans
    
    def trav(self, currP, currQ):
        if not self.ans: return
        if not currP or not currQ:
            if currP or currQ:
                self.ans = False
            return
        if currP.val != currQ.val:
            self.ans = False
        
        self.trav(currP.left, currQ.left)
        self.trav(currP.right, currQ.right)