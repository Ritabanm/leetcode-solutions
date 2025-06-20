class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for word
        j = 0  # pointer for abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False  # Leading 0 is invalid

                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num  # Skip num characters in word
            else:
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        # both should be fully consumed
        return i == len(word) and j == len(abbr)
