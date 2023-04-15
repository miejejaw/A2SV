class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        depth = 0
        
        for child in root.children:
            depth = max(depth, self.maxDepth(child))        
        return depth + 1