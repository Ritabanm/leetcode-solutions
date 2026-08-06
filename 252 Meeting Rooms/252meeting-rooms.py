"""class Solution:
    def canAttendMeetings(self,intervals):

        intervals.sort()

        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True
    
    #T: O(NLOGN), S:O(1)"""

class Solution:
    def canAttendMeetings(self,intervals):
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True
                