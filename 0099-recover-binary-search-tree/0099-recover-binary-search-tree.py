class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        st = []
        def trav(root):
            if not root: return
            
            trav(root.left)
            st.append(root)
            i,j = len(st)-2,len(st)-1
            while i>-1 and st[i].val > st[j].val:
                st[i].val,st[j].val = st[j].val,st[i].val
                i -= 1
                j -= 1            
            trav(root.right)            
        trav(root)
    # 17 00
        