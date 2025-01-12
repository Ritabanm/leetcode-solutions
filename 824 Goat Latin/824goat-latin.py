class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a','e','i','o','u', 'A', 'E','I', 'O','U'}
        res = []
        split = sentence.split()
        for i,word in enumerate(split, 1):
            cur_res = []
            if word[0] not in vowels:
                cur_res.append(word[1:] + word[0])
            else:
                cur_res.append(word)
            cur_res.append("ma")
            cur_res.extend(['a']*i)
            res.append("".join(cur_res))
        return " ".join(res)

        