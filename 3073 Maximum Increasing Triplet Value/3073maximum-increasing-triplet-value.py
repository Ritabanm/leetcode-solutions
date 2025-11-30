class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)

        right = [n - 1] * n # right[i]: index of max value for the range nums[i:]
        for i in range(n - 2, -1, -1):
            if nums[i] >= nums[right[i + 1]]:
                right[i] = i
            else:
                right[i] = right[i + 1]

        left = [-1] * n  # left[i]: index of max value for the range nums[:i] but < nums[i]
        new = sorted([(val, -1 * i) for i, val in enumerate(nums)])
        stack = []
        for _, i in new:
            while stack and stack[-1] > -1 * i:
                stack.pop()
            if stack:
                left[-1 * i] = stack[-1]
            stack.append(-1 * i)

        ans = float('-Inf')
        for i in range(1, n - 1):
            if left[i] == -1 or right[i] == i:
                continue
            ans = max(ans, nums[left[i]] + nums[right[i]] - nums[i])

        return ans