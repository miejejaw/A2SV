class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self.targetSum = targetSum
        self.helper(root,[],0)
        return self.ans
    
    def helper(self,curr,arr,total):
        if curr:
            total += curr.val
            arr.append(curr.val)
            if not curr.left and not curr.right and total == self.targetSum:
                self.ans.append(arr[:])
                arr.pop()
                return 
            
            self.helper(curr.left,arr,total)
            self.helper(curr.right,arr,total)
            arr.pop()