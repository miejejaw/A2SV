class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res,size = 0,len(skill)//2
        skill.sort()
        prev = skill[0]+skill[-1]
        for ind in range(size):
            if prev!=skill[ind]+skill[~ind]:
                return -1
            res  += skill[ind]*skill[~ind]
            
        return res