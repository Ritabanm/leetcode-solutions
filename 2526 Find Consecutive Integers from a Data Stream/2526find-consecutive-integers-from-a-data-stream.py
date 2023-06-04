class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.cnt = 0

    def consec(self, num: int) -> bool:
        self.cnt = self.cnt + 1 if num == self.v else 0
        return self.cnt >= self.k