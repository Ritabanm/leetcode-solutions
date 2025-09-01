class Solution:
    def calculateScore(self, s: str) -> int:
        mirror = {}
        aAscii = ord("a")
        zAscii = ord("z")
        iteration = 0
        for asciiVal in range(aAscii, zAscii+1):
            mirror[chr(asciiVal)] = chr(asciiVal + 25 - iteration*2)
            iteration += 1
        
        leftLetterCount = collections.defaultdict(list)
        score = 0
        for idx, letter in enumerate(s):
            if mirror[letter] in leftLetterCount:
                leftIdx = leftLetterCount[mirror[letter]].pop()
                if leftLetterCount[mirror[letter]] == []:
                    del leftLetterCount[mirror[letter]]
                score += idx - leftIdx
            else:
                leftLetterCount[letter].append(idx)

        return score