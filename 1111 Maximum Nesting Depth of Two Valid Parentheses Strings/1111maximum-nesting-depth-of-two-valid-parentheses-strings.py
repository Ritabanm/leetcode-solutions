class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack=[]
        oc=0
        res=[]
        for i in seq:
            if i=="(":
                if oc%2!=0:
                    res.append(0)
                else:
                    res.append(1)
                oc+=1
            else:
                oc-=1
                if oc%2!=0:
                    res.append(0)
                else:
                    res.append(1)
        return res