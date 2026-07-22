class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)


        #rebalancing
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                num = heapq.heappop(self.left)
                heapq.heappush(self.right, -num)
            else:
                num = heapq.heappop(self.right)
                heapq.heappush(self.left, -num)


    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()