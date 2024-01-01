class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:

        n = len(words)
        suffix = [0] * n
        prefix = [0] * n

        if n == 1:
            return [0]
            
        def lcp(s, t):
            n = min(len(s), len(t))
            i = 0
            while i < n:
                if s[i] != t[i]:
                    return i
                i+=1
                
            return i
            
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], lcp(words[i], words[i+1]))

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], lcp(words[i], words[i-1]))

        ans = []
        
        for i in range(n):
            if i-1 < 0:
                ans.append(suffix[i+1])
                continue
                
            if i+1 == n:
                ans.append(prefix[i-1])
                continue

            ans.append(max(prefix[i-1], suffix[i+1], lcp(words[i-1], words[i+1])))

        return ans
                
            