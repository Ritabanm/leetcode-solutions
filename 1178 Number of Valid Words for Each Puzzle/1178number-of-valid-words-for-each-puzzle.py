class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        d = {}
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            d[mask] = d.get(mask, 0) + 1
        ans = []
        for puzzle in puzzles:
            total = 0
            mask = 0
            for i in range(1, 7):
                mask |= 1 << (ord(puzzle[i]) - ord('a'))
            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0]) - ord('a')))
                if s in d:
                    total += d[s]
                subset = (subset - 1) & mask
            if (1 << (ord(puzzle[0]) - ord('a'))) in d:
                total += d[1 << (ord(puzzle[0]) - ord('a'))]
            ans.append(total)
        return ans