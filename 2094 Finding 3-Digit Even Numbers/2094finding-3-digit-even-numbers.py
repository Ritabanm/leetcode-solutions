class Solution:
    def findEvenNumbers(self, a: List[int]) -> List[int]:
        z = Counter(a)
        return [v for v in range(100,1000,2) if Counter(map(int,str(v)))<=z]