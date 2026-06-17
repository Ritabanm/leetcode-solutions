class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        if k == 1:
            return [n]
        root = ceil(pow(n, 1/k))
        mindiff = float("inf")
        ans = None
        while root >= 1:
            if n % root != 0:
                root -= 1
                continue
            therest = self.minDifference(n//root, k-1)
            therest.append(root)
            newdiff = max(therest) - min(therest)
            if newdiff < mindiff:
                mindiff = newdiff
                ans = therest
            root -= 1
        return ans