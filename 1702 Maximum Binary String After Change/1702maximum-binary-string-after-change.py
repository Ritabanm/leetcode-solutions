class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        arr = []
        stack = []

        for i in binary:
            stack.append(i)
            
            if stack[0] == '1':
                arr.append('1')
                stack.pop()
            elif stack[0] == '0' and stack[-1] == '0' and len(stack) > 1:
                arr.append('1')
                stack.pop()

        return ''.join(arr+stack)