class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:

        n, repeating, left = len(nums), 0, 0
        d = defaultdict(int)

        for num in nums:
            d[num]+= 1

            if d[num] == 2:
                repeating+= 1

            if repeating > k:
                d[nums[left]]-= 1

                if d[nums[left]] == 1:
                    repeating-= 1

                left+= 1

        return n - left