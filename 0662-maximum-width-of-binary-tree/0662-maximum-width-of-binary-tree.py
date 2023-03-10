class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.arr = []
        self.trav(root,0,0)
        return self.ans+1
    
    def trav(self,curr,level,wid):
        if curr:
            if level == len(self.arr):
                self.arr.append([wid,wid])
            self.trav(curr.left,level+1,wid*2)
            
            self.arr[level][1] = wid   
            self.ans = max(self.ans,wid-self.arr[level][0])
            
            self.trav(curr.right,level+1,wid*2+1)