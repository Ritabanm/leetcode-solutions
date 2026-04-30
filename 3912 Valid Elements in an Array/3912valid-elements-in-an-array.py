class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        ans =[]
        for i in range(len(nums)):
            if i==0 or i==len(nums)-1:
                ans.append(nums[i])
            else:
                try:
                    if nums[i]>max(nums[:i]) or nums[i]>max(nums[i+1:]):
                        ans.append(nums[i])
                except:
                    continue
        return ans