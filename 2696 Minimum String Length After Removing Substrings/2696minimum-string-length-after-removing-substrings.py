class Solution:
    def minLength(self, s: str) -> int:

        stack =[]
        for cur_char in s:
            if not stack:
                stack.append(cur_char)
                continue
            
            if cur_char == "B" and stack[-1]=="A":
                stack.pop()
            
            elif cur_char == "D" and stack[-1]=="C":
                stack.pop()
            else:
                stack.append(cur_char)
            
        return len(stack)