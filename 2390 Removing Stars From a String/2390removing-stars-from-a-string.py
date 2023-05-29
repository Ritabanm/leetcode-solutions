class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in range(0, len(s)):
            if s[i]=='*':
                st.pop()
            else:
                st.append(s[i])
        return ''.join(st)