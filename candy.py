class Solution:
    def candy(self, ratings: List[int]) -> int:

        length = len(ratings)
        res = [1]*length
        
        ind = 1
        while ind < length:
            while ind < length and ratings[ind-1] < ratings[ind]:
                res[ind] = max(res[ind],res[ind-1]+1)
                ind += 1
            ind += 1

        ind = length-2
        while ind >= 0:
            while ind >= 0 and ratings[ind+1] < ratings[ind]:
                res[ind] = max(res[ind],res[ind+1]+1)
                ind -= 1
            ind -= 1

        return sum(res)