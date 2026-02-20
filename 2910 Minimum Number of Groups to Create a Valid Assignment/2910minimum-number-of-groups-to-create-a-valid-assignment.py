class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        
        nums = sorted(Counter(nums).values())
        isValid = lambda k: all(num%k <= num//k for num in nums)

        for i in range(min(nums), 1, -1):
            if isValid(i):
                div = i+1
                break
        else: div = 2    

        return sum(map(lambda x: ceil(x/div), nums))