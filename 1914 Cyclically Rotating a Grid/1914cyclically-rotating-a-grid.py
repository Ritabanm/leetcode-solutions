class Solution:

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        for layer in range(min(m, n) // 2):
            top, bottom = layer, n - layer - 1
            left, right = layer, m - layer - 1

            n_layer = n - 2 * layer
            m_layer = m - 2 * layer

            size_layer = max(n_layer, m_layer) if 1 in (n_layer, m_layer) else 2 * (n_layer  + m_layer) - 4

            step = k % size_layer

            queue = []

            curr_i, curr_j = top, left
            for i in range(size_layer + step):
                queue.append(grid[curr_i][curr_j])

                if i >= step:
                   grid[curr_i][curr_j] = queue.pop(0)

                if curr_j == left and curr_i < bottom:
                    curr_i += 1
                elif curr_i == bottom and curr_j < right:
                    curr_j += 1
                elif curr_j == right and curr_i > top:
                    curr_i -= 1
                elif curr_i == top and curr_j > left:
                    curr_j -= 1

        return grid
