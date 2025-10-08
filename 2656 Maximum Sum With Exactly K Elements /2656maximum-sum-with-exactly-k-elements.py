class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        # thoughts: I think we are just going to pick the biggest number first (m), and then keep picking m + 1
        # so if we do it for k=3, we will pick m+0, m+1, m+2
        # the formula we can apply is k*m + sum([0,1, .. k-1])

        m = max(nums)

        return k*m + sum(range(k))

        # BOOM MATHS!!!! YA GIRL CAN DO MATHS