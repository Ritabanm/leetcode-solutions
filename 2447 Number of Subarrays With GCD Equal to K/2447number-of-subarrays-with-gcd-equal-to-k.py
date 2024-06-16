class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(n1, n2):
            if n2==0:
                return n1
            return gcd(n2, n1%n2)
        
        ans = 0
        n = len(nums)
        for i in range(n):
            curr_gcd = 0
            for j in range(i, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if  curr_gcd == k:
                    ans += 1
        
        return ans