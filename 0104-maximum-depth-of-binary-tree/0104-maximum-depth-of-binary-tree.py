class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.max_depth = 0
        self.findMaxDepth(root,0)
        
        return self.max_depth
    
    def findMaxDepth(self,curr,depth):
        
        if not curr:
            self.max_depth = max(self.max_depth,depth)
            return
        
        self.findMaxDepth(curr.left,depth+1)
        self.findMaxDepth(curr.right,depth+1)