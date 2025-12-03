class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        win1 = {}
        win2 = Counter(word2)
        valid = 0
        l = 0
        res = 0

        for r in range(len(word1)):
            c = word1[r]
            if c in win2:
                win1[c] = win1.get(c, 0) + 1
                if win1[c] == win2[c]: 
                    valid += 1
            while valid == len(win2):
                res += (len(word1) - r) 
                if word1[l] in win2:
                    if win1[word1[l]] == win2[word1[l]]:
                        valid -= 1
                    win1[word1[l]] -= 1
                l += 1
                
        return res