class Solution:
    def wordSquares(self, words):
        words.sort()
        res = []
        for(top, left, right, bottom) in permutations(words, 4):
            if top[0]==left[0] and top[3] == right[0]:
                if bottom[0]==left[3] and bottom[3]==right[3]:
                    res.append([top, left, right, bottom])
        return res