class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        letters = set(s)
        longest = 0

        for idx, lett in enumerate(s):
            temp = 1

            while idx + temp < len(s) and ord(lett) + temp == ord(s[idx + temp]):
                print(lett, s[temp], temp)
                temp += 1
            
            longest = max(temp, longest)

        return longest