class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        for ch in s:
            if ch == c:
                count+=1
        return count*(count-1)//2+count