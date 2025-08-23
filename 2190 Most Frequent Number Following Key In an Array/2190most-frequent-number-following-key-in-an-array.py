from collections import Counter
class Solution:
    def mostFrequent(self, nums, key):
        counts = Counter()
        for i in range(len(nums)-1):
            if nums[i]==key:
                counts[nums[i+1]]+=1
        res = max(counts, key = counts.get)
        return res
        