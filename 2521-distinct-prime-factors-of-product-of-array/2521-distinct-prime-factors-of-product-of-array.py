class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        visited = set()
        for num in nums:
            p = 2
            while p * p <= num:
                while num % p == 0:
                    visited.add(p)
                    while num % p == 0:
                        num //= p
                p += 1

            if num > 1:
                visited.add(num)
            
        return len(visited)