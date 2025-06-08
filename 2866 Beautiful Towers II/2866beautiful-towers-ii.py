class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def process(arr):
            stack = []
            n = len(arr)
            prefix = [0] * n
            for i, v in enumerate(arr):
                while stack and v < stack[-1][0]:
                    stack.pop()
                p = 0
                left = -1
                if stack:
                    left = stack[-1][1]
                    p += prefix[left]
                    
                p += (i - left) * v
                prefix[i] = p
                stack.append((v, i))
            return prefix
        left = process(maxHeights)
        right = process(maxHeights[::-1])[::-1]
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] - maxHeights[i]) 
        return ans

        
        
              