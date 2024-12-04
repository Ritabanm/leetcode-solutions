class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        counts = Counter(nums)
        outlier = float('-inf')
        for num in nums:
            remaining_sum = total_sum - num
            if remaining_sum %2 == 0:
                half = remaining_sum//2
                if half in counts:
                    if half != num or counts[half]>1:
                        outlier = max(outlier, num)
        return outlier