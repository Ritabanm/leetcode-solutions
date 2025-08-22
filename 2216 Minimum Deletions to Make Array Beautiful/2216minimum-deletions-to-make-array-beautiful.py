class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        dels = cnt = 0

        for i in range(n - 1):
            if (cnt % 2) == 0 and (nums[i] == nums[i + 1]):
                dels += 1
            else:
                cnt += 1
                
        cnt += 1         # Take the last element as it is.
        dels += cnt & 1  # If final count is odd, delete last element.
        return dels