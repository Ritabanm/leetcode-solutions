class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        ans = 0
        for i in range(len(nums)):
            ss = 0
            for j in range(i, len(nums)):
                ss+=nums[j]
                cur =str(ss)
                if cur[0]==str(x) and cur[-1]==str(x):
                    ans+=1
        return ans