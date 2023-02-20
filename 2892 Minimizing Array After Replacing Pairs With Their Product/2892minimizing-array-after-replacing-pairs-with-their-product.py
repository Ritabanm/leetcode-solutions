class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:
        ans = []
        for n in nums:
            if n==0:
                return 1
            if ans and ans[-1] *n<=k:
                ans[-1]*=n
            
            else:
                ans.append(n)
        return len(ans)