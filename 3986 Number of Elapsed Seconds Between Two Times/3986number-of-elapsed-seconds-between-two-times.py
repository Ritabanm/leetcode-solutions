"""class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st = list(map(int, startTime.split(":")))
        et = list(map(int, endTime.split(":")))
        def toTime(x):
            return (x[0]*3600) + (x[1]*60) + x[2]
        return toTime(et)-toTime(st)"""

class Solution:
    def secondsBetweenTimes(self, startTime, endTime):
        st = list(map(int, startTime.split(":")))
        et = list(map(int, endTime.split(":")))
        def toTime(x):
            return (x[0]*3600)+ (x[1]*60)+x[2]
        return toTime(et)-toTime(st)