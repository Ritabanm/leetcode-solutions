class Solution:
    def minTimeToType(self, word: str) -> int:
        store = 'a'
        res = 0

        for i in word:
            res += min(abs(ord(i) - ord(store)), (26 - abs(ord(i) - ord(store))))
            res += 1
            store = i
        
        return res