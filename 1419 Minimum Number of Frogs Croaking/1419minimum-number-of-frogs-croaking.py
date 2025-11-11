class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 0
        freq = [0]*5
        for c in croakOfFrogs:
            i = "croak".index(c)
            freq[i]+=1
            if i and freq[i-1]<freq[i]:
                return -1
            
            if c == "k":
                ans = max(ans, freq[0])
                for i in range(5):
                    freq[i]-=1
        if max(freq)==0:
            return ans
        return -1