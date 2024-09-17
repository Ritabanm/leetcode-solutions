class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        freq = defaultdict(int)
        for letter in s:
            freq[letter] += 1

        stack = []

        for letter in s:
            while stack and freq[stack[-1]] > 1 and letter < stack[-1]:
                freq[stack.pop()] -= 1
            stack.append(letter)
        while freq[stack[-1]] > 1:
            freq[stack.pop()] -= 1
            
        return "".join(stack)

        