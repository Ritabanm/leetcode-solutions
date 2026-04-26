class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        ans = [[0] * m for _ in range(n)]
        current_layer = []
        for r, c, color in sources:
            ans[r][c] = color
            current_layer.append((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while current_layer:
            next_layer_map = {}
            for r, c in current_layer:
                color = ans[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and ans[nr][nc] == 0:
                        if (nr, nc) not in next_layer_map or color > next_layer_map[(nr, nc)]:
                            next_layer_map[(nr, nc)] = color
            current_layer = []
            for (nr, nc), max_color in next_layer_map.items():
                ans[nr][nc] = max_color
                current_layer.append((nr, nc))
        return ans