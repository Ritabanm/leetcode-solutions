class Solution:
    def minSubarraySort(self, nums: list[int], k: int) -> list[int]:

        def getLeft(i: int)-> int:
            for j in range(1, k + 1):
                if nums[i + j - k] != window[j-1]: return j - 1
            return k

        def getRght(i: int)-> int:
            for j in range(i, i - k, -1):
                if nums[j] != window[k - i + j- 1]: return i - j               
            return k - 1  

            
        n = len(nums)
        window, ans = SortedList(nums[:k-1]), [0] * (n - k + 1)
        
        for i in range(k-1, n):
            
            window.add(nums[i])

            left = getLeft(i)

            if left < k:
                rght = getRght(i)
                ans[i - k + 1] = k - left - rght

            window.remove(nums[i - k + 1])

        return ans