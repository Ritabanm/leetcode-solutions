class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mini, maxi = min(nums), max(nums)
        def helper(start, arr):
            arr, ans = arr.copy(), 0
            for i in range(n):
                if start != arr[i] % 2:
                    ans += 1
                    if mini == arr[i]:
                        arr[i] += 1
                    elif maxi == arr[i]:
                        arr[i] -= 1
                start ^= 1
            return [ans, max(arr)-min(arr)]
        return min(helper(0, nums), helper(1, nums))