class Solution:
    def countHousePlacements(self, n: int) -> int:
        pre,ppre = 2,1
        if n==1:
            return 4
        for i in range(1, n):
            temp = pre+ppre
            ppre = pre
            pre = temp
        return ((pre)**2)%((10**9)+7)