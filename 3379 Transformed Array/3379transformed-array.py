class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans,length =[], len(nums)
        for idx, num in enumerate(nums):
            if num==0:
                ans.append(0)
            else:
                rem = (idx+num)%length
                ans.append(nums[rem])
        return ans