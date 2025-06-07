class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        if count[0] % 2:
            return []
        for num in sorted(count):
            if count[num] > count[2*num]:
                return []
            count[2*num] -= count[num] if num else count[0]//2
        
        return list(count.elements())