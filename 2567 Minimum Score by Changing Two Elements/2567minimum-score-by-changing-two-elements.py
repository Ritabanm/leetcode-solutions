class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        op1 = nums[-1]-nums[2]
        op2 = nums[-3]-nums[0]
        op3 = nums[-2]-nums[1]

        return min(op1,op2, op3)