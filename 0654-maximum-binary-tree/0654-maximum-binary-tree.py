# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        self.ans = None
        self.trav(nums,None,0,len(nums),"l")
        return self.ans
    
    def trav(self, nums, curr, left, right,f):
        if left < right:
            ind = self.get_max(nums,left,right)
            newNode = TreeNode(nums[ind])
            if not curr:
                self.ans = newNode
                curr = self.ans
            elif f == "l":
                curr.left = newNode
                curr = curr.left
            else:
                curr.right = newNode
                curr = curr.right
                
            self.trav(nums,curr,left,ind,"l")
            self.trav(nums,curr,ind+1,right,"r")
                
        
    def get_max(self,nums,left,right):
        
        for ind in range(left+1,right):
            if nums[ind] > nums[left]:
                left = ind
        return left