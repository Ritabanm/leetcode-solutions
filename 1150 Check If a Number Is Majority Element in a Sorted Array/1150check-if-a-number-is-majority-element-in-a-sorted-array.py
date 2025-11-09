class Solution:
    def _find_right_most(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + int((right - left) / 2)

            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return right

    def _find_left_most(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + int((right - left) / 2)

            if nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1

        return left

    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        left_most = self._find_left_most(nums, target)
        right_most = self._find_right_most(nums, target)

        return (right_most - left_most + 1) > len(nums) / 2