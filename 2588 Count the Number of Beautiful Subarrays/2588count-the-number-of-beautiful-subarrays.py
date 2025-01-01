class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        
        ctr = Counter(accumulate(nums, xor, initial = 0))

        return sum (map(lambda x: x*(x-1)//2, ctr.values()))