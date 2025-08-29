class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        if targetX == 1 and targetY == 1:
            return True
        if targetX < 1 or targetY < 1:
            return False
        if targetX % 2 == 0:
            return self.isReachable(targetX // 2, targetY)
        elif targetY % 2 == 0:
            return self.isReachable(targetX, targetY // 2)
        else:
            return self.isReachable(targetX - targetY, targetY) or self.isReachable(targetX, targetY - targetX)
            