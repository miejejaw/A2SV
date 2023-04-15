class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emps= {emp.id: emp for emp in employees}
        return self.dfs(emps,id)
    
    def dfs(self,employee,id):
        total = employee[id].importance
        for empID in employee[id].subordinates:
            total += self.dfs(employee,empID)
        return total