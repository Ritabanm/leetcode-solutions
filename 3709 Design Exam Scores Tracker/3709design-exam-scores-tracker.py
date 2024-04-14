class ExamTracker:

    def __init__(self):
        self.times=[]
        self.scores=[0]
        

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.scores.append(self.scores[-1]+score)
        

    def totalScore(self, startTime: int, endTime: int) -> int:
        l=0
        r=len(self.times)-1
        left=len(self.times)
        while(l<=r):
            mid=(l+r)//2
            if(self.times[mid]>=startTime):
                left=mid
                r=mid-1
            else:
                l=mid+1
        l=0
        r=len(self.times)-1
        right=-1
        while(l<=r):
            mid=(l+r)//2
            if(self.times[mid]<=endTime):
                l=mid+1
                right=mid
            else:
                r=mid-1
        if(left>right):
            return 0
        
        return self.scores[right+1]-self.scores[left]


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)