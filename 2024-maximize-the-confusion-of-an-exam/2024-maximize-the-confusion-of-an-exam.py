class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = 0
        beg = end = 0
        temp = k
        while len(answerKey)>end:
            if answerKey[end]=='T':
                end += 1
            elif k>0 and answerKey[end]=='F':
                end += 1
                k -= 1
            else:
                if answerKey[beg]=='F':
                    k += 1
                beg += 1
            count = max(count , end-beg)

        beg = end = 0
        k = temp
        while len(answerKey)>end:
            if answerKey[end]=='F':
                end += 1
            elif k>0 and answerKey[end]=='T':
                end += 1
                k -= 1
            else:
                if answerKey[beg]=='T':
                    k += 1
                beg += 1
            count = max(count , end-beg)
            
        return count
                