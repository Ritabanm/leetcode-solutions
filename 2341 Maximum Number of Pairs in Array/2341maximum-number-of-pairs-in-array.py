class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        single = set()
        for num in nums:
            if num in single:
                single.remove(num)
                pairs+=1
            else:
                single.add(num)
        return [pairs, len(single)]