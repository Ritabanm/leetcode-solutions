class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            is_leap_year = (
                year % 400 == 0
                or (year % 4 == 0 and year % 100 != 0)
            )
            if is_leap_year:
                return 29
        
        return days[month - 1]