class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = -1
        total,temp = 0,0
        for i in range(len(gas)):
            gas[i] -= cost[i]
            if gas[i]>=0 and idx == -1:
                idx = i
                temp = gas[i]
            total += gas[i]
            
        if total<0: return -1
        total = temp
        
        for i in range(idx+1,len(gas)):
            total += gas[i]
            if gas[i]>=0 and idx != -1:
                continue
            elif gas[i]>=0:
                idx = i
                total = gas[i]
            elif total<0:
                idx = -1
                      
        return idx
                