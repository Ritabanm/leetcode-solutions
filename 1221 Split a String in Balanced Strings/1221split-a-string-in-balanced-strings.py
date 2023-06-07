class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = prefix = 0
        for c in s:
            prefix +=1 if c=="R" else -1
            if not prefix:ans+=1
        return ans