class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        self.ans = []
        self.bfs([root])
        return self.ans

    def bfs(self, nodes):
        
        total = 0
        res = []
        length = len(nodes)
        for node in nodes:
            total += node.val
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
                
        self.ans .append(total/length) 
        if res:
            self.bfs(res)