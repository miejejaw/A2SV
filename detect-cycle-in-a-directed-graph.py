from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
		visited = set()
		for node in range(V):
		    if node not in visited:
		        if self.dfs(adj,visited,node,-1):
		            return True
		return False
		
	def dfs(self, adj, visited, curr, parent):
	    if curr not in visited:
	        visited.add(curr)
	        for node in adj[curr]:
	            if parent != node:
	                if self.dfs(adj,visited,node,curr):
	                    return True
	        return False
	    return True
	    


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends