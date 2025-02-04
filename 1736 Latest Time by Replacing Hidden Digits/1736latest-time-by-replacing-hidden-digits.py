class Solution:
    def maximumTime(self, time: str) -> str:
        h1, h2, m1, m2 = list(time.replace(":", ""))

        def hidden(s):
            return s == "?"

        if hidden(h1):
            h1 = '2' if hidden(h2) or h2 <= '3' else '1'
        if hidden(h2):
            h2 = '3' if h1 == '2' else '9'
        if hidden(m1):
            m1 = '5'
        if hidden(m2):
            m2 = '9'
        return h1 + h2 + ":" + m1 + m2