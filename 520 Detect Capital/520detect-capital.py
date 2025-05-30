class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        if len(word)==1:
            return True
        
        #case1: all capital
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if not word[i].isupper():
                    return False
            
        #Case 2 and case 3:
        else:
            for i in range(1,n):
                if word[i].isupper():
                    return False
            
        return True
        