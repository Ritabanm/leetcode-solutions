class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        gcd = math.gcd(len(arr), k)
        
        ans = 0
        for i in range(gcd):
            seq = arr[i::gcd]
            m = int(statistics.median(seq))
            for n in seq:
                ans += abs(n-m)
        return ans