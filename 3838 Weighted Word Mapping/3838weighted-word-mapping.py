class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        mapped = {0 : 'z', 1 : 'y', 2 : 'x', 3 : 'w', 4 : 'v', 5 : 'u', 6 : 't', 7 : 's', 8 : 'r', 9 : 'q', 10 : 'p', 11 : 'o', 12 : 'n', 13 : 'm', 14 : 'l', 15 : 'k', 16 : 'j', 17 : 'i', 18 : 'h', 19 : 'g', 20 : 'f', 21 : 'e', 22 : 'd', 23 : 'c', 24 : 'b', 25 : 'a'}
        ans = ''
        for word in words:
            strSum = 0
            for ch in word:
                strSum+=weights[ord(ch) - 97]
            strSum%=26
            ans+=mapped[strSum]
        return ans