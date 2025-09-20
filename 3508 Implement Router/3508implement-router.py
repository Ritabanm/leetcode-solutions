class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.dq = deque()
        self.exist = set()
        self.dl = defaultdict(deque)

    def _removeOldest_(self):
        oldest = self.dq.popleft()
        self.exist.discard(oldest)
        self.dl[oldest[1]].popleft()
        return oldest

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.exist:
            return False
        if len(self.dq) == self.limit:
            self._removeOldest_()
        self.dq.append((source, destination, timestamp))
        self.exist.add((source, destination, timestamp))
        self.dl[destination].append(timestamp)
        return True
        
    def forwardPacket(self) -> List[int]:
        if not self.dq: return []
        return self._removeOldest_()

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        tList = self.dl[destination]
        l, r = 0, len(tList) - 1
        while l <= r:
            m = l + (r - l) // 2
            if tList[m] >= startTime: r = m - 1
            else: l = m + 1
        leftMost = l

        l, r = 0, len(tList) - 1
        while l <= r:
            m = l + (r - l) // 2
            if tList[m] <= endTime: l = m + 1
            else: r = m - 1
        rightMost = r
        return rightMost - leftMost + 1