class Solution:
    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0
        for c in s:
            if c in character_set:
                character_set.remove(c)
                res+=2
            else:
                character_set.add(c)
        if character_set:
            res+=1
        return res