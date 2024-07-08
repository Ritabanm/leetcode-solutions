class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack =[]
        res =['']*len(s)
        for i,ch in enumerate(s):
            if ch == '(':
                if stack:
                    res[i]='('
                stack.append(i)
            else:
                if len(stack)>1:
                    res[i]=')'
                stack.pop()
        return "".join(res)