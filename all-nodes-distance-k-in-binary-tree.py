class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        paths = defaultdict(list)
        self.dfs(paths,root,-1)
        queue = deque([(target.val,0)])
        visited = set({target.val})
        res = []
        
        while queue:
            node,edgeCount = queue.popleft()
            if edgeCount == k:
                res.append(node)
                
            if edgeCount < k:
                edgeCount += 1
                for curr in paths[node]:
                    if curr not in visited:
                        queue.append((curr,edgeCount))
                        visited.add(curr)
                
        return res
        
        
        
    def dfs(self, paths, curr, parent):
        if curr:
            if parent != -1:
                paths[curr.val].append(parent)
                paths[parent].append(curr.val)
                
            self.dfs(paths,curr.left,curr.val)
            self.dfs(paths,curr.right,curr.val)