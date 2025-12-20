class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zeroes = 0
        ones = 0
        vc = 0
        for char in s:
            if char == '0':
                zeroes+=1
            else:
                ones+=1
            if abs(zeroes-ones)<=1:
                vc+=1
        return vc