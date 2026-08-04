class Solution:
    def beautySum(self, s: str) -> int:
        # use dictionary to store the frequencies of characters at each index and calulcate the diff b/w most frequent nd least frequent chars
        ans = 0
        n = len(s)
        for i in range(n):
            freq = {}
            maxF = 0
            for j in range(i,n):

                if s[j] in freq:
                    freq[s[j]] +=1
                
                else:
                    freq[s[j]] = 1

                maxF = max(maxF, freq[s[j]])

                minF = min(freq.values())

                ans += (maxF-minF)

        return ans

                
        