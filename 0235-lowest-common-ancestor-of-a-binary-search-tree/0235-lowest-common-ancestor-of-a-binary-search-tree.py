class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root,p,q)
    def helper(self,curr,p,q):
        if curr:
            if p == curr or q == curr:
                return curr
            
            left = self.helper(curr.left,p,q)
            right = self.helper(curr.right,p,q)
            if left and not right:
                return left
            elif not left and right:
                return right
            elif left and right:
                return curr
            
        return None