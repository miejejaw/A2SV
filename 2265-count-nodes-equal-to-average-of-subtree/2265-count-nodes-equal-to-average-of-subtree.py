class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.findAverage(root)
        return self.ans
    
    def findAverage(self,curr):
        if curr:
            left = self.findAverage(curr.left)
            right = self.findAverage(curr.right)
            total = left[0] + right[0] + curr.val
            numberOfnodes = left[1] + right[1] + 1
            if curr.val == total//numberOfnodes:
                self.ans += 1
            return [total,numberOfnodes]
        
        return [0,0]