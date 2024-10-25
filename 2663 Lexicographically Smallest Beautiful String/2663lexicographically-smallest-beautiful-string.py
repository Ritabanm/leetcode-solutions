class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        s = list(s)
        i = len(s) - 1
        s[i] = chr(ord(s[i]) + 1)
        while 0 <= i < len(s):
            if ord(s[i]) - ord('a') >= k:
                s[i] = 'a'
                i -= 1
                s[i] = chr(ord(s[i]) + 1)
            elif (i >= 1 and s[i] == s[i - 1]) or (i >= 2 and s[i] == s[i - 2]):
                s[i] = chr(ord(s[i]) + 1)
            else:
                i += 1
        return '' if i < 0 else ''.join(s)