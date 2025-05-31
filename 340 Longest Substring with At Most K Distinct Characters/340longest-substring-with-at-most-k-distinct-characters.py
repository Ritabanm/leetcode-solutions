class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        maxSize = 0
        counter= collections.Counter()

        for r in range(len(s)):
            counter[s[r]]+=1

            if len(counter)<=k:
                maxSize+=1
            
            else:
                counter[s[r-maxSize]] -=1
                if counter[s[r-maxSize]]==0:
                    del counter[s[r-maxSize]]
        return maxSize