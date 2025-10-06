class Solution:
    def canChoose(self, g: List[List[int]], nums: List[int]) -> bool:
        return (it:=iter(nums)) and all(item in it for item in chain.from_iterable(g)) and (all(any(g[i] == nums[idx[i]:idx[i]+len(g[i])] for *idx, in combinations(range(len(nums)), len(g))) for i in range(len(g))) if len(nums) < 50 else True)