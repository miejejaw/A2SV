class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n -= 1
        m -= 1
        i = len(nums1)-1
        for _ in range(len(nums1)):
            if m>=0 and n>=0 and nums1[m]>=nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            elif n>=0:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
        