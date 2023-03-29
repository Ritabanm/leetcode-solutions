class LUPrefix:

    def __init__(self, n: int):
        self.videos = [False] * (n + 1)
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.videos[video-1] = True

    def longest(self) -> int:
        while self.videos[self.prefix]:
            self.prefix += 1
        return self.prefix