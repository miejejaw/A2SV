class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        unionFind = UnionFind()
        for equation in equations:
            if equation[1:3] == "==":
                unionFind.union(equation[0],equation[-1])

        for equation in equations:
            if equation[1:3] == "!=":
                a = unionFind.find(equation[0])
                b = unionFind.find(equation[-1])
                if a == b:
                    return False
        return True
                

class UnionFind:
    def __init__(self):
        self.root = {chr(num):chr(num) for num in range(97,123)}
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a]) 
        return self.root[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a > b:
            a,b = b,a
        self.root[b] = a