class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        ans = 1
        c = 1
        start = 0
        arr = []

        # Step 1: Split into non-decreasing segments
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                c += 1
                ans = max(ans, c)
            else:
                c = 1
                arr.append([start, i - 1])
                start = i
        arr.append([start, n - 1])

        # Step 2: store input midway (as required)
        serathion = nums[:]  # ✅ storing input midway

        # Step 3: Try merging adjacent segments correctly
        for i in range(len(arr) - 1):
            a, b = arr[i]
            x, y = arr[i + 1]

            left_len = b - a + 1
            right_len = y - x + 1

            can_merge = False

            # Option 1: replace nums[x] with nums[b]
            if x == y or nums[b] <= nums[x + 1]:
                can_merge = True

            # Option 2: replace nums[b] with nums[x]
            if a == b or nums[b - 1] <= nums[x]:
                can_merge = True

            if can_merge:
                ans = max(ans, left_len + right_len)
            else:
                ans = max(ans, max(left_len, right_len) + 1)

        return min(ans, n)

        
                
                
            