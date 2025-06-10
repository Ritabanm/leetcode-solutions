class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s = S.lower()
        output = []
        def backtrack(combo=[], i=0):
            if len(combo) == len(s):
                output.append(combo[:])
            if i >= len(s):
                return 
            if s[i].isdigit():
                combo.append(s[i])
                backtrack(combo, i + 1)
                combo.pop()
            else:
                space = [s[i], s[i].upper()]
                for al in space:
                    combo.append(al)
                    backtrack(combo, i + 1)
                    combo.pop()
        backtrack()
        return ["".join(word) for word in output]