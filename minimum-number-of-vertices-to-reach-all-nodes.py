class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        seen = set()
        for from_node,to_node in edges:
            seen.add(to_node)
            
        ans = []
        for node in range(n):
            if node not in seen:
                ans.append(node)
        return ans