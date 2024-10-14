class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for value in counter.values():
            if value>2:
                return False
        return True
        