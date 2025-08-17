class StatisticsTracker:

    def __init__(self):
        self.d = deque()
        self.s = SortedList()
        self.freq = defaultdict(int)
        self.biggestf = 0
        
    def addNumber(self, number: int) -> None:
        self.d.append(number)
        self.freq[number] += 1
        self.s.add(number)

    def removeFirstAddedNumber(self) -> None:
        if self.d:
            a = self.d.popleft()
            self.freq[a] -= 1
            if self.freq[a] == 0:
                del self.freq[a]

            if a in self.s:
                self.s.remove(a)
      
    def getMean(self) -> int:
        ans = floor(sum(self.d) // len(self.d))
        return ans
        
    def getMedian(self) -> int:
        if len(self.s) % 2 == 0:
            mid = len(self.s) // 2
            return self.s[mid]
        else:
            mid = len(self.s) // 2 
            if mid >= 0 and mid < len(self.s):
                return self.s[mid]
            else:
                return self.s[0]
        
    def getMode(self) -> int:
        biggest = max(self.freq.values())
        ans = float('inf')
        for a, b in self.freq.items():
            if b == biggest:
                ans = min(ans, a)
        return ans
        


# Your StatisticsTracker object will be instantiated and called as such:
# obj = StatisticsTracker()
# obj.addNumber(number)
# obj.removeFirstAddedNumber()
# param_3 = obj.getMean()
# param_4 = obj.getMedian()
# param_5 = obj.getMode()