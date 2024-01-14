class Solution:
    def shortestSequence(self, rolls: list[int], k: int) -> int:
        seen = [False] * (k + 1)
        cnt, passes = 0, 0
        for roll in rolls:
            if not seen[roll]:
                seen[roll] = True
                cnt += 1
                if cnt == k:
                    passes += 1
                    seen = [False] * (k + 1)
                    cnt = 0
        return passes + 1 