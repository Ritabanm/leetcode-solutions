class Solution:
    def processStr(self, s: str) -> str:

        r = ""

        a = ['#','%','*']

        for c in s:

            if c not in a:

                r+=c


            if c == "#":

                r+=r

            if c == "%":

                r = r[::-1]

            if c == "*":

                r = r[:-1]


        return r
        