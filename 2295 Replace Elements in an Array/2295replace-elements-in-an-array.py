class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]]=i
        print(seen)

        for i in range(len(operations)):
            ix = seen.get(operations[i][0])
            nums[ix]=operations[i][1]
            seen.pop(operations[i][0])
            seen[operations[i][1]] = ix
        return nums