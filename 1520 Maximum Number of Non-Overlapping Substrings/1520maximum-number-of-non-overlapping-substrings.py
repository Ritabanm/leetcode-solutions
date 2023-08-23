class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        m={}
        for i,ch in enumerate(s):
            if ch not in m: m[ch]=[i,i]
            else: m[ch][1] = i
        res, st, start = [], [], -1
        for ind,ch in enumerate(s):
            if st and st[-1][1] == ind:
                i,j,_ = st.pop()
                if i>start:
                    res.append(s[i:j+1])
                start=j
                continue
            i,j = m[ch]
            setch = {ch}
            if i==j:
                res.append(s[i])
                start=j
                continue
            while st and (st[-1][0]>=i or st[-1][1]<=j or ch in st[-1][2]):
                x = st.pop()
                i,j = min(i, x[0]), max(j, x[1])
                setch.update(x[2])
            st.append((i,j,setch))
        return res
            
        