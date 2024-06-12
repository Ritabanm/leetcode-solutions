class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:

        n, ans = len(nums)//2, 0
        smLft, smRgt = sum(nums[:n]), sum(nums[n:])

        for lft, rgt in zip(nums[:n], nums[n:]):
            ans+= (smLft != smRgt)
            smLft+= rgt - lft
            smRgt-= rgt - lft

        return ans