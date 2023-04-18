class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.preorder(root)
    
    def preorder(self,curr):
        if curr:
            left = self.preorder(curr.left)
            right = self.preorder(curr.right)
            if left or right:
                left = f"({left})"
            if right:
                right = f"({right})"
            return str(curr.val)+left+right
        
        return ""