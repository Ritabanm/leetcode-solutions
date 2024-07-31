class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n, indices = len(nums), defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        ans = n        
        for l in indices.values():
            l.append(l[0] + n)
            ans = min(ans, max(y - x for x, y in pairwise(l)) // 2)
        return ans
        