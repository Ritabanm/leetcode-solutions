class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        word = ''
        leng = len(s)
        for i in range(leng):
            word+=s[(i+k)%leng]
        return word
        