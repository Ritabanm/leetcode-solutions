class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        mini = abs(n-k)
        maxi = n+k
        res = 0
        for num in range(maxi+1):
            if (abs(num-n)<=k and num&n==0):
                res+=num
        return res