class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0 
        emps= {emp.id: emp for emp in employees}
        def helper(id: int):
            nonlocal total
            total += emps[id].importance
            for i in emps[id].subordinates:
                helper(i)
        helper(id)
        return total
        
#10 57