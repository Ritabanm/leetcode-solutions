class Solution:
    def numJewelsInStones(self, J, S):
        JSet = set(J)
        return sum(s in JSet for s in S)
