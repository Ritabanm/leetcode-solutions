class Solution:
    from itertools import combinations
    hours = (1, 2, 4, 8)
    minutes = (1, 2, 4, 8, 16, 32)

    def makeValidTime(self, hour: int, minute: int):
        if minute > 59 or hour > 11:
            return 
        else:
            hour = str(hour)
            minute = str(minute)
            if len(minute) == 1:
                minute = "0" + minute
            return hour + ":" + minute

    def possible_hours(self, num):
        return set(map(sum, combinations(self.hours, num)))

    def possible_mins(self, num):
        return set(map(sum, combinations(self.minutes, num)))

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = set()
        pairs = []
        pos_hours = set()
        pos_mins = set()
        for num_hours in range(0, turnedOn + 1):
            for num_minutes in range(0, turnedOn + 1):
                if num_hours + num_minutes == turnedOn:
                    ans = ans.union(
                        {
                        self.makeValidTime(hour, minute) for hour in self.possible_hours(num_hours) for minute in self.possible_mins(num_minutes) 
                        }
                    )
        if None in ans:
            ans.remove(None)
        return list(ans)