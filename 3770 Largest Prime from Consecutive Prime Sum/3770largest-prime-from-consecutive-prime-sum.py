class Solution:
    def largestPrime(self, n: int) -> int:

        def isPrime(cand: int) -> bool: 
            for num in range(3, isqrt(cand) + 1, 2):
                if cand %num == 0: return False
            return True


        if n == 1: return 0
        ans = sm = 2

        for num in range(3, n, 2):
            if sm + num > n: return ans
            if isPrime(num):
                sm+= num
                if sm %2 == 1 and isPrime(sm):
                    ans = sm
        return ans