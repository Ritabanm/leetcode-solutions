class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        mapping = {}

        for x in queries[::-1]:
            mapping[x] = None
        
        for x in windows:
            mapping[x] = None
        
        return [x for x in mapping.keys()]