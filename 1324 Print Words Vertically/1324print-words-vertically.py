class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = len(max(s, key = len))

        ans = []
        for i in range(n):
            curr = ''
            for word in s:
                if len(word)>i:
                    curr+= word[i]
                else:
                    curr += ' '
            ans.append(curr.rstrip())
        return ans