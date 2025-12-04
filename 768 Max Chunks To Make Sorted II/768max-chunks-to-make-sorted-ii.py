class Solution(object):
    def maxChunksToSorted(self, arr):
        stack = []
        for x in arr:
            if not stack or x>=stack[-1]:
                stack.append(x)
            else:
                m = stack.pop()
                while stack and x<stack[-1]:
                    stack.pop()
                stack.append(m)
        return len(stack)