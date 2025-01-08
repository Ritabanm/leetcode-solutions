class Solution:
    def oddString(self, words: List[str]) -> str:
        def find_dif(word):
            return [ord(word[i+1])-ord(word[i]) for i in range(len(word)-1)]

        difs=[find_dif(word) for word in words]

        for index,i in enumerate(difs):
            if difs.count(i)==1:
                return words[index]
            