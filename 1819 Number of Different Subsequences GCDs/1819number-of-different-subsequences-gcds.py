class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        m = max(nums)
        for i in range(1, m+1):
            if i in s:
                count+=1
                continue
            gcd = 0
            for j in range(2, m//i+1):
                if j*i not in s:
                    continue
                gcd = math.gcd(gcd, j)
                if gcd ==1 :
                    count+=1
                    break
        return count