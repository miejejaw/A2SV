"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0       
        def helper(id: int):
            nonlocal total
            for i,val in enumerate(employees):
                if val.id == id:
                    id = i
                    break            
            total += employees[id].importance
            for i in employees[id].subordinates:
                helper(i)
        helper(id)
        return total
        
#10 57