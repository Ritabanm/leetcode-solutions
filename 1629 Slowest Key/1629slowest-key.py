class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        slowest = releaseTimes[0]
        key = keysPressed[0]
        n = len(releaseTimes)
        for i in range(n-1):
            time = releaseTimes[i+1] - releaseTimes[i]
            if time > slowest:
                slowest = time
                key = keysPressed[i+1]
            elif time == slowest:
                key = chr(max(ord(key),ord(keysPressed[i+1])))
        return key