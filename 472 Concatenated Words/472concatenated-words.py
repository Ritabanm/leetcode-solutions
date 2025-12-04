class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        res = []

        def can_form(word):
            n = len(word)
            dp = [False]*(n+1)
            dp[0] = True
            for i in range(1, n+1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[n]

        for w in words:
            word_set.remove(w)
            if can_form(w):
                res.append(w)
            word_set.add(w)
        return res