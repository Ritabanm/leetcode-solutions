class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        while nums:
            freq = nums[0]
            val = nums[1]

            arr +=[val]*freq
            nums = nums[2:]
        return arr
        