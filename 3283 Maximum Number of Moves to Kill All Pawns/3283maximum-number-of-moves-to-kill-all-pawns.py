class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        dx = [-2, -1, +1, +2, +2, +1, -1, -2]
        dy = [+1, +2, +2, +1, -1, -2, -2, -1]
        n = len(positions)

        @cache
        def capturePawn(kkx, kky, pos):
            moves = 0

            q = [[kkx, kky]]
            vis = [[False for _ in range(50)] for _ in range(50)]
            vis[kkx][kky] = True

            while True:
                ll = len(q)
                for i in range(ll):
                    current = q.pop(0)
                    if current[0] == pos[0] and current[1] == pos[1]:
                        return moves

                    for j in range(8):
                        nextX = current[0] + dx[j]
                        nextY = current[1] + dy[j]

                        if 0 <= nextX <= 49 and 0 <= nextY <= 49:
                            if not vis[nextX][nextY]:
                                vis[nextX][nextY] = True
                                q.append([nextX, nextY])

                moves += 1

            # use bfs
            return moves

        fin = (1 << n) - 1

        @cache
        def dp(alice: bool, state: int, kkx, kky):
            if state == fin:
                return 0
            score = -1

            if alice:
                # chose the option which gives the maximum sum of moves in the end
                for i in range(n):
                    if state & (1 << i) == 0:
                        current = capturePawn(kkx, kky, tuple(positions[i]))

                        if score == -1:
                            score = current + dp(False, state | (1 << i), positions[i][0], positions[i][1])
                        else:
                            score = max(score, current + dp(False, state | (1 << i), positions[i][0], positions[i][1]))
            else:
                # chose the option which gives the minimum sum of moves in the end
                for i in range(n):
                    if state & (1 << i) == 0:
                        current = capturePawn(kkx, kky, tuple(positions[i]))

                        if score == -1:
                            score = current + dp(True, state | (1 << i), positions[i][0], positions[i][1])
                        else:
                            score = min(score, current  + dp(True, state | (1 << i), positions[i][0], positions[i][1]))
            return score

        return dp(True, 0, kx, ky)