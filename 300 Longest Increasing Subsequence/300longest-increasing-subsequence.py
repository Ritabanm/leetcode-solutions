import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            # Find the position where num should go using binary search
            idx = bisect.bisect_left(sub, num)
            
            # If num is larger than all elements in sub, it extends our longest subsequence
            if idx == len(sub):
                sub.append(num)
            # Otherwise, replace the existing element to keep potential tails tight/small
            else:
                sub[idx] = num
                
        return len(sub)