class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        count_chars = Counter(nums)
        freq = Counter(count_chars.values())

        for qty, cnt in freq.items():
            if cnt==1: break
        else:
            return -1
        
        for num, val in count_chars.items():
            if val==qty: return num