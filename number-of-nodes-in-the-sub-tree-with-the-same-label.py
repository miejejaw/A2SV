class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
         
        paths = defaultdict(list)
        for a,b in edges:
            paths[a].append(b)
            paths[b].append(a)
        ans = [0]*n
        self.dfs(paths,labels,ans,0)
        return ans
    
    def dfs(self, paths, labels, res, curr):
        
        subtreeLabelCount = [0]*26
        while paths[curr]:
            node = paths[curr].pop()
            paths[node].remove(curr)
            temp = self.dfs(paths,labels,res,node)
            self.addArrays(subtreeLabelCount,temp)
            
        ind = ord(labels[curr])-97
        subtreeLabelCount[ind] += 1
        res[curr] = subtreeLabelCount[ind]
        return subtreeLabelCount
            
    def addArrays(self, array1, array2):
        for ind in range(26):
            array1[ind] += array2[ind]