class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        stack = []
        for i, x in enumerate(nums + [0]): 
            while stack and stack[-1][1] >= x: 
                _, xx = stack.pop()
                k = i-stack[-1][0]-2 if stack else i-1
                ans[k] = max(ans[k], xx)
            stack.append((i, x))
        
        for i in reversed(range(len(nums)-1)): 
            ans[i] = max(ans[i], ans[i+1])
        return ans