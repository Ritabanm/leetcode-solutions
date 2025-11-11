class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        @cache
        def dist(dx, dy) -> float:
            return math.sqrt(dx**2 + dy**2)

        best_coords, best_quality = [-1, -1], -1
        for x in range(51):
            for y in range(51):
                towers_in_range = [t for t in towers if dist(t[0] - x, t[1] - y) <= radius]
                quality = 0
                for t in towers_in_range: quality += int(t[2] / (1 + dist(t[0] - x, t[1] - y)))
                if quality > best_quality:
                    best_quality = quality
                    best_coords = [x, y]
        return best_coords
                