class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        n = len(words)
        mn = float("inf")
        for i,w in enumerate(words):
            if w==target:
                d = i-startIndex if i-startIndex>=0 else i-startIndex+n
                mn = min(mn, min(d,n-d))

        return mn