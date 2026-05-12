class Solution:
    def resultingString(self, s: str) -> str:
        st = []

        for c in s:
            if (st and (ord(st[-1]) == ord(c)-1 or ord(st[-1])==ord(c)+1
            or (st[-1]=="z" and c=="a") or (st[-1]=="a" and c=="z"))):
                st.pop()
            else:
                st.append(c)

        return "".join(st)