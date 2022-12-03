
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        st,ans = [], 0
        def helper(root):
            nonlocal ans
            if not root: return
            if len(st)>1 and st[-2]%2==0:
                ans += root.val
            st.append(root.val)
            helper(root.left)
            helper(root.right)
            del st[-1]
        helper(root)
        return ans
            
        