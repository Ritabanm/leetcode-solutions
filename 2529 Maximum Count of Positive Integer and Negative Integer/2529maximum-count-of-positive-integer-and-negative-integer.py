class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_c = 0
        neg_c = 0
        for num in nums:
            if num>0:
                pos_c+=1
            elif num<0:
                neg_c +=1
        return max(pos_c, neg_c)