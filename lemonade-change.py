class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        money = {5:0,10:0}
        for order in bills:
            if order == 5:
                money[5] += 1
            elif order == 10:
                if money[5] == 0: return False
                money[5] -= 1
                money[10] += 1
            else:
                if money[10] and money[5]: 
                    money[5] -= 1
                    money[10] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else: 
                    return False

        return True