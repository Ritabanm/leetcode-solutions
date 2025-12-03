class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        fountstr = ''

        # Iterate over each character in the target string
        for i, char in enumerate(target):
            s = 'a'
            # Append the current state of fountstr + the starting 'a'
            res.append(fountstr + s)
            # Increment 's' until it matches the target character
            while char != s:
                s = chr(ord(s) + 1)
                res.append(fountstr + s)
            # Update fountstr to include the current character
            fountstr += s

        return res