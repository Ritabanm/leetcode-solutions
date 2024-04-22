class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviations = dict()
        for d in dictionary:
            abbreviation = self._abbreviation(d)
            # If abbreviation already exists and maps to a different word, mark it as non-unique
            if abbreviation in self.abbreviations and self.abbreviations[abbreviation] != d:
                self.abbreviations[abbreviation] = None
            else:
                self.abbreviations[abbreviation] = d

    def isUnique(self, word: str) -> bool:
        abbreviation = self._abbreviation(word)
        # A word is unique if its abbreviation doesn't exist or it maps exactly to itself
        if abbreviation not in self.abbreviations:
            return True
        elif self.abbreviations[abbreviation] == word:
            return True
        return False
    
    def _abbreviation(self, word):
        # Abbreviation format: (first char, length of middle part, last char)
        if len(word) <= 2:
            return word
        return (word[0], len(word) - 2, word[-1])