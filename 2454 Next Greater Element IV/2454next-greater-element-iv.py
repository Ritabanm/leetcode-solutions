class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)  # Initialize result array with -1
        stack = []  # Monotonic decreasing stack for elements waiting for first greater
        s2 = deque()  # Queue for elements waiting for second greater
        
        for i, n in enumerate(nums):
            # Check if current element is the second greater for any element in s2
            while s2 and nums[s2[-1]] < n:
                res[s2.pop()] = n  # Found second greater, update result
            
            # Check if current element is the first greater for any element in stack
            tmp = []
            while stack and nums[stack[-1]] < n:
                tmp.append(stack.pop())  # Found first greater
            
            # Add elements that found their first greater to s2 (in reverse to maintain order)
            s2 += tmp[::-1]
            
            # Add current element to the stack
            stack.append(i)
            
        return res