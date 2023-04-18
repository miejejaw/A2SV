class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0)
    
    def dfs(self, curr, total):
        if curr:
            total = total*10 + curr.val
            if not curr.left and not curr.right:
                return total
            left = self.dfs(curr.left,total)
            right = self.dfs(curr.right,total)
            return left+right
        return 0