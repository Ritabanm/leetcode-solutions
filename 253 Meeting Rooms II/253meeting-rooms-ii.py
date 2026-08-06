class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        ptr1 = 0
        ptr2 = 0
        rooms = 0

        while ptr1<len(intervals):
            if start[ptr1]<end[ptr2]:
                rooms+=1
            else:
                ptr2+=1
            ptr1+=1
        return rooms

        #T: O(NLogN), S: O(N)