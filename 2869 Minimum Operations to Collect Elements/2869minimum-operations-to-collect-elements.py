class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        need = set(range(1, k+1))
        operations = 0

        for i in range(len(nums)-1, -1, -1):
            operations += 1
            if nums[i] in need:
                need.remove(nums[i])
                
                if len(need) == 0:
                    return operations
            
            

        return operations