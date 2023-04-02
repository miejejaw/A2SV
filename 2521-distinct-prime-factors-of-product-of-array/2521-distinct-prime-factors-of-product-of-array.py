class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        visited = set()
        for num in nums:
            mult = 2
            temp = num

            while mult * mult <= num:
                while temp % mult == 0:
                    temp //= mult
                    visited.add(mult)
                mult += 1

            if temp > 1:
                visited.add(temp)
            
        return len(visited)