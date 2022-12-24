class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        total_salary = sum(salary)-min_salary-max_salary
        average_salary = round(total_salary / (len(salary)-2) , 5)
        return average_salary