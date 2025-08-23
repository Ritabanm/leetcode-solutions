class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year,month,day = date.split('-')
        y = bin(int(year))[2:]
        m = bin(int(month))[2:]
        d = bin(int(day))[2:]
        return f"{y}-{m}-{d}"