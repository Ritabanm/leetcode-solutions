class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        m = {}
        count = 1
        for i, k in enumerate(nums):
            if k == x:
                m[count] = i
                count +=1
        sol = []
        for i in queries:
            if i in m:
                sol.append(m[i])
            else:
                sol.append(-1)
        return sol