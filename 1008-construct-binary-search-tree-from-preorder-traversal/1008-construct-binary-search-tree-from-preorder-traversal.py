class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        length = len(preorder)
        ans = TreeNode(preorder[0])
        st = [ans]
        for ind in range(1,length):
            temp = None
            while st and st[-1].val < preorder[ind]:
                temp = st.pop()
                
            newNode = TreeNode(preorder[ind])            
            if temp :
                temp.right = newNode
            else:
                st[-1].left = newNode
                
            st.append(newNode)
            
        return ans