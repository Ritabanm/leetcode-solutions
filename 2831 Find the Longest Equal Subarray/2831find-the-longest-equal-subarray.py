class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ## store elements in a dictionary 
        ## while sum(dictionary.values) - dictionary.max > k:
            ## window is too large, dictionary[s[left]] -= 1
        count = defaultdict(int)
        left,right,max_length,max_freq= 0,0,0,0
        
        while right < len(nums):
            count[nums[right]] += 1
            max_freq = max(max_freq, count[nums[right]])
            while (right - left + 1) - max_freq > k:
                count[nums[left]] -= 1
                left += 1

            remove = right - left + 1 - max_freq
            max_length = max(max_length, right - left + 1 - remove)
            right += 1
        return max_length



        