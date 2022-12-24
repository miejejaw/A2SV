class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total_salary = sum(salary)
        total_salary -= salary[0]+salary[-1]
        average_salary = "{0:.5f}".format(total_salary / (len(salary)-2))
        return float(average_salary)