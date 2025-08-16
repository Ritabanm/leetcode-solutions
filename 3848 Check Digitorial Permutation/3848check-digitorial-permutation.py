class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:

        def fact(digit: int, res = 1) -> int:
            for i in range(2, int(digit) + 1):
                res*= i
            return res

        n = str(n)
        if len(n) not in {1,3,5}: return False
        sm = sum(map(fact, n))
        return sorted(str(sm)) == sorted(n)