class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:

        def updateMasks(num, seen1, seen2, seen3):

            mask = seen3 & num
            mask, seen1 = num & seen1, seen1 ^ (num & seen1) | mask
            mask, seen2 = num & seen2, seen2 ^ (num & seen2) | mask
            mask, seen3 = num & seen3, seen3 ^ (num & seen3) | mask
            return seen1, seen2, seen3

       
        seen1, seen2, seen3 = -1, 0, 0 
       
        for num in nums:
            seen1, seen2, seen3 = updateMasks( num, seen1, seen2, seen3)

        mask2, mask3 = seen2, seen3
        seen1, seen2, seen3 = -1, 0, 0
 
        for num in nums:
            if ~num & mask2 or num & mask3: continue
            seen1, seen2, seen3 = updateMasks(num, seen1, seen2, seen3)

        return [seen2, (seen2 ^ mask2) | mask3]