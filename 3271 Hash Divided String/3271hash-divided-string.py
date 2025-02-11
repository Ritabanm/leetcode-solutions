class Solution:
    def stringHash(self, s: str, k: int) -> str:
        total = ""
        def counter(subs):
            summ = 0
            for i in subs:
                summ += ord(i) - 97
            return chr((summ%26)+97)

        for i in range(0, len(s), k):
            total += counter(s[i:i+k])
        return total