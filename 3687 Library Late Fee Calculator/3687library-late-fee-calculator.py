class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        return reduce(lambda acc,curr: acc + ((curr*3 if curr > 5 else ( curr*2 if curr >=2 else 1))), daysLate,0)