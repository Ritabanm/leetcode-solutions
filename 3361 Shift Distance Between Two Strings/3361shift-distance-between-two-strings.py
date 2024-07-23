class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        totalcost = 0
        for i in range(len(s)):
            start = ord(s[i]) - ord('a')
            end = ord(t[i]) - ord('a')
            if start == end: continue

            forward = (end - start + 26) % 26
            forwardcost = 0
            for j in range(forward):
                forwardcost += nextCost[(start+j)%26]

            backward = (start - end + 26) % 26
            backwardcost = 0
            for j in range(backward):
                backwardcost += previousCost[(start-j)%26]

            totalcost += min(forwardcost, backwardcost)
        return totalcost