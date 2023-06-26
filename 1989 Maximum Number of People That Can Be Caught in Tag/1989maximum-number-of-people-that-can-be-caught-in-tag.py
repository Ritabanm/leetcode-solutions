class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        if len(team) == 1 or dist == 0 or len(team) == sum(team): return 0
        caught = 0

        if dist >= len(team):
            return min(sum(team), len(team)-sum(team))

        i,j = -1,-1
        for _ in range(len(team)):
            if i != -1 and j != -1: break
            elif i == -1 and team[_] == 1: 
                i = _
            elif j == -1 and team[_] == 0: 
                j = _
        
        while i < len(team) and j < len(team):
            while i < j and j-i > dist: i += 1
            while j < i and i-j > dist: j += 1
            if team[i] == 1 and team[j] == 0: 
                caught += 1
                team[i] == -1
                team[j] == -1
                i += 1
                j += 1
            elif team[i] != 1: i += 1
            elif team[j] != 0: j += 1


        return caught