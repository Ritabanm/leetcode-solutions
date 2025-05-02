class Solution: # June 12, 2025 Revision
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:

        nums.sort()
        if nums[-1] > target: return False

        accumProd = list(accumulate(nums, mul))
        if accumProd[-1] != target * target: return False

        mid = (len(nums)+1)//2 
        for prod in accumProd[ :mid]:
            if prod > target: return False

        return True 