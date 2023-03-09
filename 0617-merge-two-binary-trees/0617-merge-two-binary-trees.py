class Solution:
    def mergeTrees(self, root1, root2) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 if root1 else root2
        
        self.merge(root1,root2)
        return root1
    
    def merge(self,curr1,curr2):
        
        if curr1 and curr2:
            curr1.val += curr2.val
            left = self.merge(curr1.left,curr2.left)
            if left:
                curr1.left = left
            right = self.merge(curr1.right,curr2.right)
            if right:
                curr1.right = right
                
        elif not curr1 and curr2:
            return curr2
            
        