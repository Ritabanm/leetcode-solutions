class Solution:
    def countWays(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        prev = float("inf")

        # Select None
        if nums[0] > 0:
            res += 1

        for i in range(len(nums) - 1, -1, -1):
            selected = i + 1

            # 1st condition: Total # selected students > nums[i]
            # 2nd condition: All non-selected students' value are > # of selected students
            if selected > nums[i] and prev > selected:
                res += 1
            prev = nums[i]
        return res