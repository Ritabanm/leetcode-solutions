class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        res = []
        
        for i in nums:
            res.append(int(i))
        
        res.sort(reverse = True)
        
        return str(res[k-1])