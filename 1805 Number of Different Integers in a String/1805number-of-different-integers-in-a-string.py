class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers = set()
        number = []
        for char in word:
            if char.isdigit():
                number.append(char)
            elif number:
                numbers.add(int(''.join(number)))
                number = []
        if number:
                numbers.add(int(''.join(number)))
        return len(numbers)