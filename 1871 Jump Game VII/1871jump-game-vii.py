class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # we can move the goalpost back anywhere between min/max jump

        # so all we need to do is start at the end, and move the goal post back between max, and min jump
        # we start at the max jump, and see if it is reachable, if not go to the next spot 
        n = len(s)
        goal = n - 1
        if s[goal] == "1":
            return False
        q = deque()
        q.append(0)
        farthest = 0
        while q:
            index = q.popleft()
            start = max(index + minJump, farthest + 1)
            end = min(index + maxJump, n - 1)
            for i in range(start, end + 1):
                if s[i] == "0":
                    q.append(i)
                if i == goal:
                    return True
            farthest = end
        return False