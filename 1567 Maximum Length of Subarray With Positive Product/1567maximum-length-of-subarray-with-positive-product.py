class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        curLenPos = 0
        curLenNeg = 0
        ans = 0
        for num in nums:
            if num > 0:
                curLenPos,curLenNeg = curLenPos + 1, curLenNeg + 1 if curLenNeg != 0 else 0
            elif num < 0:
                curLenNeg,curLenPos = curLenPos + 1, curLenNeg + 1 if curLenNeg != 0 else 0
            else:
                curLenNeg = 0
                curLenPos = 0
            ans = max(ans,curLenPos)
            
        return ans
            