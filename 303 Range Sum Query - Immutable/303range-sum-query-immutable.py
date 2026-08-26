class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix.append(nums[i]+self.prefix[i-1])        

    def sumRange(self, left: int, right: int) -> int:
        if left ==0:
            return self.prefix[right]
        else:
            return self.prefix[right]-self.prefix[left-1]
