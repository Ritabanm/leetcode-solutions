class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        pI, PN = [],[]
        for idx, num in enumerate(nums):
            if num<0: continue
            pI.append(idx)
            PN.append(num)
        
        p = len(pI)
        if p<=1: return nums
        k%=p
        if k==0: return nums
        rotNum = PN[k:]+PN[:k]
        for idx, num in zip(pI, rotNum):
            nums[idx]=num
        return nums