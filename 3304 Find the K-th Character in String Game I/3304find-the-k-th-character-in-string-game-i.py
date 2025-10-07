class Solution:
    def sol(self,word,k):
        if len(word)>k:
            return word
        t=""
        for i in word:
            if i=="z":
                t+="a"
            else:
                t+=chr(ord(i)+1)
        word=word+t
        return self.sol(word,k)
    def kthCharacter(self, k: int) -> str:
        s=self.sol("a",k)
        return s[k-1]