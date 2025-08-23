class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n = ans = len(nums)
        seen = [False] * n

        digSum = lambda x: (sum(map(int, str(nums[x]))), nums[x])

        perm = sorted(range(n), key = digSum)

        for i in range(n):
            if seen[i]: continue
            ans-= 1
            curr = i
            
            while not seen[curr]:
                seen[curr] = True
                curr = perm[curr]

        return ans