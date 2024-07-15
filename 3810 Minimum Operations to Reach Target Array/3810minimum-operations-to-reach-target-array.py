class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        ans = set()
        for num, tar in zip(nums, target):
            if num == tar:
                continue
            ans.add(num)
        return len(ans)