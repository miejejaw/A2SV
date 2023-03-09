class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.level = 0
        self.trav(root,0)
        return self.ans
    def trav(self,curr,ind):
        if curr:
            if ind == self.level:
                self.ans.append([])
                self.level += 1
            self.ans[ind].append(curr.val)
            self.trav(curr.left,ind+1)
            self.trav(curr.right,ind+1)
#10