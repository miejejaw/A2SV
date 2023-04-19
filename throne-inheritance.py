class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingdom = defaultdict(list)
        self.kingName = kingName
        self.deathNames = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deathNames.add(name)

    def getInheritanceOrder(self) -> List[str]:
        inheritanceOrder = []
        self.dfs(inheritanceOrder, self.kingName)
        return inheritanceOrder
    
    def dfs(self, inheritanceOrder, parent):
        
        if parent not in self.deathNames:
            inheritanceOrder.append(parent)
        for child in self.kingdom[parent]:
            self.dfs(inheritanceOrder,child)