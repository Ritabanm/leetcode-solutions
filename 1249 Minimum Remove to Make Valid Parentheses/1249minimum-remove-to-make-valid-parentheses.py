class Solution:
    def minRemoveToMakeValid(self, s: str):
        result = []
        open_count = 0
        for char in s:
            if char == '(':
                open_count+=1
            elif char == ')':
                if open_count==0:
                    continue 
                open_count-=1
            result.append(char)
        open_count = 0
        final_result = []
        for char in reversed(result):
            if char == '(':
                if open_count==0:
                    continue
                open_count-=1
            elif char==')':
                open_count+=1
            final_result.append(char)
        return ''.join(reversed(final_result))