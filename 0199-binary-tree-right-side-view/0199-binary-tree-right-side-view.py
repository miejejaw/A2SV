class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.level = 0
        self.trav(root,0)
        return self.ans
    def trav(self,curr,ind):
        if curr:
            if ind == self.level:
                self.ans.append(curr.val)
                self.level += 1
                
            self.ans[ind] = curr.val
            self.trav(curr.left,ind+1)
            self.trav(curr.right,ind+1)