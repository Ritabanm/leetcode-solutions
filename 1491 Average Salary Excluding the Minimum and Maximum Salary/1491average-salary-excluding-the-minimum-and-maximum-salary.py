class Solution:
    def average(self, salary: List[int]) -> float:
        mi, ma = min(salary), max(salary)
        salary.remove(mi)
        salary.remove(ma)
        return sum(salary)/len(salary)