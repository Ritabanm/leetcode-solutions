class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # horizontal and vertical four directions 
        for direction in [[1,0],[-1,0],[0,1],[0,-1]]:
            dx, dy = direction
            for i in range(1,8):
                # if we spot bishop just break, because the rook may be in a blind spot to queen. no need to check further
                if e + i*dx == c and f + i*dy == d:
                    break
                # if we spot rook , we can capture queen in 1 move
                if e + i*dx == a and f + i*dy == b:
                    return 1
        # move in diagonal four directions 
        for direction in [[1,1],[-1,-1],[-1,1],[1,-1]]:
            dx, dy = direction
            for i in range(1,8):
                # if we spot rook just break, because the bishop may be in a blind spot. no need to check further
                if e + i*dx == a and f + i*dy == b:
                    break
                # if we spot bishop , we can capture queen in 1 move
                if e + i*dx == c and f + i*dy == d:
                    return 1
        return 2
        