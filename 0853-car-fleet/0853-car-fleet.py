class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        time = [0]*length
        for i in range(length):
            time[i] = (position[i],(target-position[i])/speed[i]) 
        
        st = []
        for pos,t in sorted(time):
            while st and st[-1] <= t:
                st.pop()
            st.append(t)
            
        return len(st)