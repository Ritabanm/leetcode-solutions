class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        res=[]
        def backT(index, subset, temp):
            if(index==len(subset) or subset[-1]=="0"):
                if(subset=="0" or subset[0]!="0"):
                    temp.append(subset)
                return
            temp.append(subset[:index]+"."+subset[index:])
            if(subset[0]=="0"):
                return
            backT(index+1,subset,temp)

        for j in range(2, len(s) - 1):
            a = s[1:j]
            b = s[j:-1]
            m=[]
            n=[]
            backT(1, a, m)
            backT(1, b, n)
            z = ["(" + p + ", " + q + ")" for q in n for p in m]
            res.extend(z)
        return res