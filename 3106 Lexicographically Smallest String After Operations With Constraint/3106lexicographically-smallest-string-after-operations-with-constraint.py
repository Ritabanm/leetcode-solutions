class Solution:
    def getSmallestString(self, s: str, k: int, ans = '' ) -> str:

        for i, num in enumerate(map(lambda x: ord(x) - 97, s)):
                                                # <--1)
            dist = min(num, 26 - num)
            if dist <= k:                       # <--2)
                k-= dist
                ans+= 'a'
            else: 
                ans+= chr(num + 97 - k)         # <--3)
                break

        return ans + s[i+1:]                    # <--4)