class Solution:
    def residuePrefixes(self, s: str) -> int:
        result, uniq = 0, set()
        for i, char in enumerate(s):
            uniq.add(char)
            if len(uniq) == (i+1)%3:
                result+=1
            elif len(uniq)>2:
                break
        return result