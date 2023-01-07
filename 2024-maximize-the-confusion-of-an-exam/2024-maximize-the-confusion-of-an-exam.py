class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = 0
        a,b = 'T','F'
        for _ in range(2):
            beg = end = 0 
            rev = k
            while len(answerKey)>end:
                if answerKey[end]==a:
                    end += 1
                elif rev>0 and answerKey[end]==b:
                    end += 1
                    rev -= 1
                else:
                    if answerKey[beg]==b:
                        rev += 1
                    beg += 1
                count = max(count , end-beg)

            a = 'F'
            b = 'T'
           
        return count
                