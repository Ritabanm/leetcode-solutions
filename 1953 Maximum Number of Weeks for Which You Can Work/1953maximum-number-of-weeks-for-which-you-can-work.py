class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m = max(milestones)
        s = sum(milestones)
        if s<2*m:
            return (2*(s-m)+1)
        return s