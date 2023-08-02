class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def rec(ind, path=[]):
            if len(path) > 1:
                yield path
            for i in range(ind, len(nums)):
                if not path or nums[i] >= path[-1]:
                    yield from rec(i+1, path+[nums[i]])
        return list(set(tuple(i) for i in rec(0)))