class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i]==ch:
                part1 = word[:i+1]
                part1 = part1[::-1]
                part2 = word[i+1:]
                return part1+part2
        return word