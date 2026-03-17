class VideoSharingPlatform:

    def __init__(self):
        self.h = []
        for i in range(10**5 + 5):
            heapq.heappush(self.h, i)
        self.lookup = {}
        self.likes = defaultdict(int)
        self.dislikes = defaultdict(int)
        self.views = defaultdict(int)

        

    def upload(self, video: str) -> int:
        video_id = heapq.heappop(self.h)
        self.lookup[video_id] = video
        return video_id

    def remove(self, videoId: int) -> None:
        if videoId in self.lookup:
            del self.lookup[videoId]
            self.likes[videoId] = 0
            self.dislikes[videoId] = 0
            self.views[videoId] = 0
            heapq.heappush(self.h, videoId)
        

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.lookup:
            return "-1"
        s = self.lookup[videoId][startMinute:endMinute+1]
        self.views[videoId] += 1
        return s

    def like(self, videoId: int) -> None:
        if videoId not in self.lookup:
            return

        self.likes[videoId] += 1
        

    def dislike(self, videoId: int) -> None:
        if videoId not in self.lookup:
            return

        self.dislikes[videoId] += 1
    

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.lookup:
            return [-1]

        return [self.likes[videoId], self.dislikes[videoId]]
        

    def getViews(self, videoId: int) -> int:
        if videoId not in self.lookup:
            return -1

        return self.views[videoId]
        


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)