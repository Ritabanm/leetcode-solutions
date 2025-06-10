class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:

        arr, stack = [1] * len(nums), deque()

        for i, num in enumerate(nums):
            while stack and num >= nums[stack[0]]:

                idx = stack.popleft()
                arr[i]+= arr[idx]*(num == nums[idx])
                
            stack.appendleft(i)

        return sum(arr)