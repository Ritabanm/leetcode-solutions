class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        
        n = len(nums)//2
        pairs = list(map(sorted, zip(nums[:n], nums[-1:n-1:-1])))

        differences = sorted(max(k - x, y) for x, y in pairs)
        ctr = Counter(map(lambda x: x[1] - x[0], pairs))

        return min(bisect_left(differences, key)
                                 + n - ctr[key] for key in ctr)