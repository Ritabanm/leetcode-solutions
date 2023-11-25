class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse = True)
        top_k = nums[:k]
        total_sum = 0
        for ch in top_k:
            if mul>1:
                total_sum+=ch*mul
                mul-=1
            else:
                total_sum+=ch
        return total_sum