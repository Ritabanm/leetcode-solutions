class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper_case_letters = ''
        lower_case_letters = ''
        my_set = set()

        for i in word:
            if i.isupper():
                upper_case_letters = upper_case_letters + i
            else:
                lower_case_letters = lower_case_letters + i

        for j in upper_case_letters:
            if j in lower_case_letters.upper():
                my_set.add(j)

        return len(my_set)
                