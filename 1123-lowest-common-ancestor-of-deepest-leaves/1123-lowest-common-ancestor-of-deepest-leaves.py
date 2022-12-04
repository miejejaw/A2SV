# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans,m = root,0
        def trav(root,i):
            nonlocal m,ans
            if not root:
                m = max(m,i)
                return i
                        
            l = trav(root.left,i+1)
            r = trav(root.right,i+1)
            if l==r and l==m: ans = root
            return max(l,r)
        trav(root,0)
        return ans
            
        
        
#15 48
        