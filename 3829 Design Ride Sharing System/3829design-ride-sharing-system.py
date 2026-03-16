class RideSharingSystem:

    def __init__(self):
        self.r = set()
        self.d = set()
        self.qr = deque()
        self.qd = deque()

    def addRider(self, riderId: int) -> None:
        if riderId not in self.r:
            self.r.add(riderId)
            self.qr.append(riderId)

    def addDriver(self, driverId: int) -> None:
        if driverId not in self.d:
            self.d.add(driverId)
            self.qd.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.qr and self.qd:
            while self.qr:
                rider = self.qr.popleft()
                if rider in self.r:
                    if rider in self.r:
                        driver = self.qd.popleft()
                        self.r.remove(rider)
                        self.d.remove(driver)
                        return [driver, rider]
        return [-1,-1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.r:
            self.r.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)