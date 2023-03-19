class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = defaultdict(list)
        self.trav(root,0,0)
        ans = []
        for ind in sorted(self.res):
            temp = self.res[ind]
            temp.sort(key = lambda x : (x[0],x[1]))
            row = []
            for r in temp:
                row.append(r[1])
            ans.append(row)
            
            
        return ans
        
    def trav(self,curr,row,col):
        if curr:
            self.res[col].append((row,curr.val))
                
            self.trav(curr.left, row+1, col-1)
            self.trav(curr.right, row+1, col+1)