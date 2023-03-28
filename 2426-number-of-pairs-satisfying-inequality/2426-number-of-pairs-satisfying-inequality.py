class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.length = len(nums1)
        self.ans = 0 
        self.diff = diff
        self.mergeSort(nums1,nums2,0,self.length-1)
        return self.ans
    
    def mergeSort(self,nums1,nums2,left,right):
        if left == right:
            return [nums1[left]-nums2[left]]
        
        mid = left + (right-left)//2
        leftArr = self.mergeSort(nums1,nums2,left,mid)
        rightArr = self.mergeSort(nums1,nums2,mid+1,right)
        self.countPairs(leftArr,rightArr)
        return self.merge(leftArr,rightArr)
    
    def merge(self,leftArr,rightArr):
        left_len = len(leftArr)
        right_len = len(rightArr)
        i,j = 0,0
        res = []
        while i < left_len and j < right_len:
            if leftArr[i] <= rightArr[j]:
                res.append(leftArr[i])
                i += 1
            else:
                res.append(rightArr[j])
                j += 1
        return res + leftArr[i:] + rightArr[j:]
    def countPairs(self,leftArr,rightArr):
        count = 0
        
        for num in rightArr:
            num = num + self.diff
            for ind in range(count,len(leftArr)):
                if num < leftArr[ind]:
                    break
                count += 1
            self.ans += count
                    