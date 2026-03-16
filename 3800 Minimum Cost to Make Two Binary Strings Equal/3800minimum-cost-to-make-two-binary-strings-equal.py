class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        c = defaultdict(int)
        total =0
        for x in range(len(s)):
            if s[x] != t[x]:
                if s[x] == "0":
                    c["01"] = c["01"] + 1
                else:
                    c["10"] = c["10"] + 1
                total = total + 1
        ans = total * flipCost
        a = abs(c["01"] - c["10"])
        b = min(c["01"], c["10"])
        
        t = b * swapCost
        if a % 2 == 0:
            ans =  min(ans, t + (a//2) * (swapCost + crossCost))
        else:
            ans =  min(ans, t + ((a -1) // 2) * (swapCost + crossCost) + flipCost)
    
        ans = min(ans, t + a * flipCost)
        return ans
          
        

        
        
        