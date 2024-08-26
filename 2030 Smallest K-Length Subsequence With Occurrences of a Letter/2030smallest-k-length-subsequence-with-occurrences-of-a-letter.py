class Solution:
    def smallestSubsequence(self, s, k, letter, repetition):
        n, count, stack = len(s), sum(x == letter for x in s), []

        for i,j in enumerate(s):
            while stack and stack[-1] > j and len(stack) + n - i > k and (stack[-1] != letter or repetition < count):
                if stack.pop() == letter: repetition += 1

            if len(stack) < k and (j == letter or len(stack) + repetition < k):
                stack.append(j)
                if j == letter: repetition -= 1

            if j == letter: count -= 1

        return "".join(stack)

        






        
        