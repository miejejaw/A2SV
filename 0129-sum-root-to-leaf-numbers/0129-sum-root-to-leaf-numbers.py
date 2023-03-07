
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root,0)
        return self.ans
    
    def helper(self,curr,num):
        if curr:
            if not curr.left and not curr.right:
                self.ans += num*10 + curr.val
                return
            num = num*10+curr.val

            self.helper(curr.left,num )
            self.helper(curr.right, num)
        