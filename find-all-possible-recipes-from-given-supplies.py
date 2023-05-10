class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        length = len(recipes)
        graph,indegree = self.buildAdList(recipes,ingredients,supplies,length)
        
        queue = deque()
        for ind in range(length):
            if recipes[ind] not in indegree:
                queue.append(recipes[ind])
                       
        res = []
        while queue:
            recipe = queue.popleft()
            res.append(recipe)
            
            for neighbour in graph[recipe]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                
                
        return res
        
        
    def buildAdList(self,recipes,ingredients,supplies,length):
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        supplies = set({*supplies})
        
        for ind in range(length):
            for ingredient in ingredients[ind]:
                if ingredient not in supplies:
                    graph[ingredient].append(recipes[ind])
                    indegree[recipes[ind]] += 1
                    
        return graph,indegree