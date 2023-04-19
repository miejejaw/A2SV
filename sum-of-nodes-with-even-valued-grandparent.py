class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        return self.dfs(root,None,None)
    
    def dfs(self, curr, grandparent, parent):
        if curr:
            total = 0
            if grandparent and grandparent.val%2 == 0:
                total += curr.val
            total += self.dfs(curr.left,parent,curr)
            total += self.dfs(curr.right,parent,curr)
            return total
        return 0