class Solution:
    def lengthOfLIS(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        ans = []
        ans.append(arr[0])

        for i in range(1, n):
            if arr[i] > ans[-1]:
                ans.append(arr[i])
            else:
                low = 0
                high = len(ans) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if ans[mid] < arr[i]:
                        low = mid + 1
                    else:
                        high = mid
                ans[low] = arr[i]

        return len(ans)

    def longestSubsequence(self, nums: List[int]) -> int:
        arr = [[] for _ in range(32)]   # fixed initialization
        ans = 0                         # initialize ans

        for x in nums:
            for i in range(0, 32):
                if x & 2**i:
                    arr[i].append(x)

        for x in arr:
            ans = max(ans, self.lengthOfLIS(x))

        return ans