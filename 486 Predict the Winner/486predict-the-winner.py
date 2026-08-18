class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)
        def maxDiff(l,r):
            if l==r:
                return nums[l]
            score_by_left = nums[l]-maxDiff(l+1,r)
            score_by_right = nums[r]-maxDiff(l,r-1)
            return max(score_by_left, score_by_right)
        return maxDiff(0, n-1)>=0