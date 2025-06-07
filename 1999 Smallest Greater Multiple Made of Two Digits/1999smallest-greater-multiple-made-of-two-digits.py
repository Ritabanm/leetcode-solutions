from collections import deque
class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        q = deque()
        d1 = min(digit1,digit2)
        d2 = max(digit1,digit2)
        if d1!= 0:
            q.append(d1)
        if d2!= 0:
            q.append(d2)
        maxInt = 2**31-1
        while(q):
            nextInteger = q.popleft()
            if nextInteger > maxInt: return -1
            elif nextInteger > k and nextInteger % k == 0: return nextInteger

            q.append(nextInteger*10+d1)
            q.append(nextInteger*10+d2)
        return -1

        