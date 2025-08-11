class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        d = dict((itm[0] , itm[1]) for itm in knowledge )

        new = ''
        cur = ''
        b = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                while s[i] != ')':
                    cur += s[i]
                    i += 1
                if cur in d:
                    new += d[cur]
                else:
                    new += '?'
                cur = ''
            else:
                new += s[i]
            i += 1

        return new
           