class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.ans = None
        self.helper(nums,None,0,len(nums),0)
        return self.ans

    def helper(self,nums,curr,left,right,f):

        if left < right:

            mid = (right+left)//2
            temp = TreeNode(nums[mid])

            if not self.ans:
                self.ans = temp
                curr = temp
            elif f == 0:
                curr.left = temp
                curr = curr.left
            else:
                curr.right = temp
                curr= curr.right

            self.helper(nums,curr,left,mid,0)
            self.helper(nums,curr,mid+1,right,1)
