class Solution:
    def isValid(Self, s):
        if not s:
            return 0
        stack = []
        mapping = {"}":"{", "]":"[", ")":"("}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else 0
                if mapping[char]!=top_element:
                    return False
            else:
                stack.append(char)
        return not stack
        #T: O(N), S:O(N)