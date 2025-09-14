class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        check_word, check_capitlization, check_vowels = {*wordlist}, {}, {}
        for word in wordlist:
            if (key_l := word.lower()) not in check_capitlization:
                check_capitlization[key_l] = word
            if (key_v := ''.join((ch, '*')[ch in 'aeiou'] for ch in key_l)) not in check_vowels:
                check_vowels[key_v] = word

        ans = []
        for query in queries:
            if query in check_word:
                ans.append(query)
            elif (key_l := query.lower()) in check_capitlization:
                ans.append(check_capitlization[key_l])
            elif (key_v := ''.join((ch, '*')[ch in 'aeiou'] for ch in key_l)) in check_vowels:
                ans.append(check_vowels[key_v])
            else:
                ans.append('')
        return ans