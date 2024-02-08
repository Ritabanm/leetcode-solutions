class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1, nums2):
            n = len(nums1)
            dp = [[0] * 3 for _ in range(n+1)]

            dp[0][2] = float('-inf')

            for i in range(1, n+1):
                dp[i][0] = dp[i-1][0] + nums1[i-1]
                dp[i][1] = max(dp[i-1][0] + nums2[i-1], dp[i-1][1] + nums2[i-1])
                dp[i][2] = max(dp[i-1][2] + nums1[i-1], dp[i-1][1] + nums1[i-1])
            
            return max(dp[-1])
        
        return max(helper(nums1, nums2), helper(nums2, nums1))