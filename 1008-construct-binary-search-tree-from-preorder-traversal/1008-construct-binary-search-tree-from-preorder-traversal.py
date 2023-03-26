class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.length = len(preorder)
        self.ans = TreeNode(preorder[0])
        self.helper(preorder,1,[self.ans])
        return self.ans
    
    def helper(self,preorder,ind,st):
        if ind < self.length:
            temp = None
            while st and st[-1].val < preorder[ind]:
                temp = st.pop()
                
            newNode = TreeNode(preorder[ind])            
            if temp :
                temp.right = newNode
            else:
                st[-1].left = newNode
                
            st.append(newNode)
            self.helper(preorder,ind+1,st)