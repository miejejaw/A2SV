class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        beg,end = 0,len(people)-1
        while end>=beg:
            if people[end]==limit or people[beg]+people[end]>limit:
                count += 1
                end -= 1
            else:
                count += 1
                end -= 1
                beg += 1
        return count
            