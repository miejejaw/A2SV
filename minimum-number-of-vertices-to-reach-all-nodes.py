class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        startingNodes = set()
        seen = set()
        for from_node,to_node in edges:
            if from_node not in seen:
                startingNodes.add(from_node)
                seen.add(to_node)
            if to_node in startingNodes:
                node = startingNodes.remove(to_node)
                seen.add(node)
            seen.add(to_node)

        return list(startingNodes)