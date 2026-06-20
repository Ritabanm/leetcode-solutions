class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        s = s[0] + s+ s[-1]
        arr = [i for i in range(len(s)-1) if s[i]==s[i+1]]
        return max((y-x for x,y in zip(arr, arr[2:])),default = len(s)-2)
        