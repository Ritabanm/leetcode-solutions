class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res , s = float('inf'), set()
        for a in arr:
            s = {a&b for b in s}| {a}
            res = min(res, min(abs(a-target) for a in s))
        return res