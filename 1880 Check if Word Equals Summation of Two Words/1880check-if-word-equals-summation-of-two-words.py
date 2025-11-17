class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getValue(s):
            res = 0
            val = 10**(len(s)-1)
            for i in s:
                res+= (ord(i)-ord("a"))*val
                val/=10
            return res
        return getValue(firstWord)+getValue(secondWord) == getValue(targetWord)