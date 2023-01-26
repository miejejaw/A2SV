class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        beg,end = 0,len(people)-1
        while end>=beg:
            if people[beg]+people[end]<=limit:
                beg += 1  
                
            end -= 1
            count += 1
                
        return count
            