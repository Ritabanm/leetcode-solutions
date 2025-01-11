class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.strip().split(' ')
        res = 0

        for word in words:
            if not word:
                continue

            if not self.valid_characters(word):
                continue

            if not self.valid_punctuation(word):
                continue

            if '-' in word and not self.valid_hyphen(word):
                continue
            
            res += 1
        return res
    
    def valid_characters(self, word):
        for char in word:
            if char.isdigit():
                return False
        return True

    def valid_punctuation(self, word):
        n = len(word) - 1
        for idx, char in enumerate(word):
            if char in '!,.' and idx != n:
                return False
        return True
    
    def valid_hyphen(self, word):
        split_word = word.split('-')

        if len(split_word) > 2:
            return False

        for w in split_word:
            char_count = 0
            for char in w:
                if char.isdigit():
                    return False
                
                if char not in '!,.':
                    char_count += 1
            
            if char_count == 0:
                return False
        return True