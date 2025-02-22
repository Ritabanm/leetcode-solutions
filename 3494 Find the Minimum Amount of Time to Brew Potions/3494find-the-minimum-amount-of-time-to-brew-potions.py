class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        time = [0]*(len(skill))
        prev = 0
        for i in range(len(mana)):
            t = time[0]+mana[i]*skill[0]
            for j in range(1, len(skill)):
                t = max(t, time[j])+mana[i]*skill[j]
            for j in range(len(skill)-1, -1, -1):
                time[j]=t
                t-= mana[i]*skill[j]
        return time[-1]