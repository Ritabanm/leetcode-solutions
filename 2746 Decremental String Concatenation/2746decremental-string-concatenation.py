class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        
        @lru_cache(None)
        def dp(aLft,aRgt,idx):

            if idx == len(words): return 0

            wLft, wRgt = words[idx][0], words[idx][-1]
            
            return max((wRgt==aLft) + dp(wLft,aRgt,idx+1), 
                       (aRgt==wLft) + dp(aLft,wRgt,idx+1))
        
        return sum(map(len, words)) - dp(words[0][0],words[0][-1],1)