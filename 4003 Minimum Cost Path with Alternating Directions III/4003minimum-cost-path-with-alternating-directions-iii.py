class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        import math
        # dist[r][c][p] where p is 0 for odd-numbered action, 1 for even-numbered action
        dist = [[[math.inf, math.inf] for _ in range(n)] for _ in range(m)]
        
        # Start at (0, 0) with initial cost (0+1)*(0+1) = 1
        # The next move is Action 1 (odd-numbered), so parity = 0.
        initial_cost = 1
        dist[0][0][0] = initial_cost
        
        # Heap: (cost, r, c, parity)
        pq = [(initial_cost, 0, 0, 0)]
        
        while pq:
            cost, r, c, p = heapq.heappop(pq)
            
            if cost > dist[r][c][p]:
                continue
                
            if r == m - 1 and c == n - 1:
                return cost
                
            # If next action is odd (p == 0): valid moves are DOWN and RIGHT
            # If next action is even (p == 1): valid moves are UP and LEFT
            
            # Let's define all possible moves: (nr, nc, is_valid_by_parity_rule)
            # Odd action (p=0): right (c+1), down (r+1) are valid. up (r-1), left (c-1) are violations.
            # Even action (p=1): up (r-1), left (c-1) are valid. right (c+1), down (r+1) are violations.
            
            moves = []
            # Down: (r + 1, c)
            if r + 1 < m:
                valid = (p == 0)
                moves.append((r + 1, c, valid))
            # Right: (r, c + 1)
            if c + 1 < n:
                valid = (p == 0)
                moves.append((r, c + 1, valid))
            # Up: (r - 1, c)
            if r - 1 >= 0:
                valid = (p == 1)
                moves.append((r - 1, c, valid))
            # Left: (r, c - 1)
            if c - 1 >= 0:
                valid = (p == 1)
                moves.append((r, c - 1, valid))
                
            # Option 1: Move to adjacent cells
            for nr, nc, valid in moves:
                entry_cost = (nr + 1) * (nc + 1)
                extra_cost = 0 if valid else penalty[r][c]
                next_cost = cost + entry_cost + extra_cost
                next_parity = 1 - p
                
                if next_cost < dist[nr][nc][next_parity]:
                    dist[nr][nc][next_parity] = next_cost
                    heapq.heappush(pq, (next_cost, nr, nc, next_parity))
                    
            # Option 2: Wait in the current cell (r, c)
            # Waiting counts as an action! The action number increases by 1, so parity flips.
            wait_cost = cost + penalty[r][c]
            next_parity = 1 - p
            if wait_cost < dist[r][c][next_parity]:
                dist[r][c][next_parity] = wait_cost
                heapq.heappush(pq, (wait_cost, r, c, next_parity))
                
        return -1