class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.helper(root,"")
        return self.ans
    
    def helper(self,curr,path):
        if curr:
            if not curr.left and not curr.right:
                self.ans.append(path+str(curr.val))
                return
            path += str(curr.val)+"->"   
            self.helper(curr.left,path)
            self.helper(curr.right,path)
#10