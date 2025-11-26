class Solution:
    ntow = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def countOddLetters(self, n: int) -> int:
        cnts = Counter(''.join([self.ntow[int(d)] for d in str(n)]))
        return sum([c % 2 for c in cnts.values()])