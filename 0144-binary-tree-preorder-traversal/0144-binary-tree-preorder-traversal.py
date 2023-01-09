class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.trav(root,ans)
        return ans
    def trav(self, curr, ans):
        if not curr:
            return
        ans.append(curr.val)
        self.trav(curr.left,ans)
        self.trav(curr.right,ans)