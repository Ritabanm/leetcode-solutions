class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n1, n2 = len(word1), len(word2)

        right_matches = [0] * (n1) # right_matches[i] = no. of matched characters (from the right) of word2 from index i+1 in word1

        j = n2-1 #pointer for word2 from right
        matches = 0 #counter for word2 matches from the right
        for i in range(n1-1,0,-1):
            if matches == n2:
                pass
            elif word1[i] == word2[j]:
                j -= 1
                matches += 1
            right_matches[i-1] = matches
        # print("right_matches", right_matches)
        output = []
        j = 0 #reset j pointer to left of word2
        mismatch = 1 #allow 1 mismatch
        for i in range(n1):
            if word1[i] == word2[j]:
                output.append(i)
                j += 1
            else:
                if mismatch > 0:
                    if right_matches[i] >= n2 - len(output) -1 : # enough matches to its right, can use mismatch here
                        output.append(i)
                        mismatch -= 1
                        j += 1
            if j == n2:
                return output
        return []