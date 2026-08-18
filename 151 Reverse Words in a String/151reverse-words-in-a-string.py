"""class Solution:
    def reverseWords(self, s:str)->str:
        n = len(s)
        word = ""
        stack = []

        for i in range(n):
            if s[i]!= " ":
                word += s[i]
            else:
                if word:
                    stack.append(word)
                    word = ""
        if word:
            stack.append(word)
        
        return " ".join(stack[::-1])"""

class Solution:
    def reverseWords(self, s):
        n = len(s)
        word = ""
        stack = []
        for i in range(n):
            if s[i]!= " ":
                word+=s[i]
            else:
                if word:
                    stack.append(word)
                    word = ""
        if word:
            stack.append(word)
        return " ".join(stack[::-1])