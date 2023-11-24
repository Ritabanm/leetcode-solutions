class Solution:
    def twoSum(self, nums, target):
        #Edge case empty nums
        if not nums or len(nums)==0:
            return []
        
        #Logic: hashmap and compliment to optimize for space usage.

        hashmap = {}
        for i in range(len(nums)):
            compliment = target-nums[i]
            if compliment in hashmap:
                return [i, hashmap[compliment]]
            hashmap[nums[i]]=i
        
        #T:O(N), S:O(1)