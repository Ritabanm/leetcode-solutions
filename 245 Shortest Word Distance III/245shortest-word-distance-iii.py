class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        selected_word = None
        looking_for = None
        position, min_pos = 0, len(words)
        for i, w in enumerate(words):
            if w != word1 and w != word2:
                continue

            if not selected_word:
                selected_word = w

                if w == word1:
                    looking_for = word2
                else:
                    looking_for = word1

                position = i
                continue

            # We must check if w == looking_for first as in the case where word1 == word2,
            # w == selected_word == looking_for
			
			# If we're looking for a and a in [a,b,a,c]
            # When we encounter the second a, we must compute the distance. If the `if-else` were reversed,
			# we would refresh the position, whereas we found what we were looking for.
			
            # If we're looking for a and c in [a b a c],
            # We must 'refresh' a's position when we find the second occurrence.

            if w == looking_for:
                min_pos = min(min_pos, i - position)
                selected_word, looking_for = looking_for, selected_word
                position = i
            else:
                position = i

        return min_pos