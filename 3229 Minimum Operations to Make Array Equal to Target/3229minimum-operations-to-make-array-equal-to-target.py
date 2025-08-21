class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

        diffs = [0] + list(map(sub, target, nums)) + [0]

        return sum(y - x for x, y in pairwise(diffs) if x < y)