class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        cur_sum = sum(nums)
        diff = abs(goal-cur_sum)
        min_ele = (diff+limit-1)//limit
        return min_ele