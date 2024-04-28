class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        min_num = min(nums)
        nums_set = set(nums)
        range_nums = set(range(min_num,min_num + len_nums))
        return range_nums.difference(nums_set) == set()