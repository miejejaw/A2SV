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
        for i,val in enumerate(employees):
            if val.id == id:
                id = i
                break            
        for i in employees[id].subordinates:
            total += self.getImportance(employees,i)
        total += employees[id].importance
        return total
        
#10 57