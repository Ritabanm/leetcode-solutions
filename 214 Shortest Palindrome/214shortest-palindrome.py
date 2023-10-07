class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        #Reversing the string
        reversed_string = s[::-1]
        #Iterate through string & find longest prefix.
        for i in range(length):
            if s[:length-i]==reversed_string[i:]:
                return reversed_string[:i]+s
        return ""