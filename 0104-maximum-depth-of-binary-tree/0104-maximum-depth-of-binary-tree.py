class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.max_depth = 0
        self.findMaxDepth(root,1)
        return self.max_depth
    
    def findMaxDepth(self,curr,depth):
        if not curr:
            return
        self.max_depth = max(self.max_depth,depth)
        self.findMaxDepth(curr.left,depth+1)
        self.findMaxDepth(curr.right,depth+1)