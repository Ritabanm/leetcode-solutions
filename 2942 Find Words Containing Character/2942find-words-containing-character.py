class Solution:
    def findWordsContaining(self, words:List[str],x:str):
        if not words:
            return []
        

        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res