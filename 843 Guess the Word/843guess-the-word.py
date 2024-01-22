class Solution:
    def getMatch(self,word1, word2):
        count = 0
        for x,y in zip(word1,word2):
            if x == y:
                count +=1
        return count
                
            
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        i = 0
        matches = 0
        while i <10 and matches !=6:
            index = random.randint(0,len(wordlist)-1)
            word = wordlist[index]
            matches = master.guess(word)
            candidates = []
            for w in wordlist:
                if matches == self.getMatch(word,w):
                    candidates.append(w)
            wordlist = candidates
        return word