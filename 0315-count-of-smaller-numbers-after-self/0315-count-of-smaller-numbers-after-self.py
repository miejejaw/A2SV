class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.length = len(nums)
        self.ans = [0]*self.length 
        self.mergeSort(nums,0,self.length-1)
        return self.ans
    
    def mergeSort(self,nums,left,right):
        if left == right:
            return [(nums[left],left)]
        
        mid = left + (right-left)//2
        leftArr = self.mergeSort(nums,left,mid)
        rightArr = self.mergeSort(nums,mid+1,right)
        self.countPairs(leftArr,rightArr)
        return self.merge(leftArr,rightArr)
    
    def merge(self,leftArr,rightArr):
        left_len = len(leftArr)
        right_len = len(rightArr)
        i,j = 0,0
        res = []
        while i < left_len and j < right_len:
            if leftArr[i][0] <= rightArr[j][0]:
                res.append(leftArr[i])
                i += 1
            else:
                res.append(rightArr[j])
                j += 1
        return res + leftArr[i:] + rightArr[j:]
    def countPairs(self,leftArr,rightArr):
        count = 0
        for num in leftArr:
            for ind in range(count,len(rightArr)):
                if num[0] <= rightArr[ind][0]:
                    break
                count += 1
            self.ans[num[1]] += count
        