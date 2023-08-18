class Solution:
    def repeatedCharacter(self, s: str) -> str:
        result =[]
        for i in range(len(s)):
            if s[i] in result:
                return s[i]
            else:
                result.append(s[i])