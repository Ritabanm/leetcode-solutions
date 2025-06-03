class Solution:
    def reformatDate(self, date: str) -> str:
        ans = ''
        date = date.split()
        for i in date[0]:
            if i.isdigit():
                ans += i
        if len(ans) == 1:
            ans = '0' + ans
        ans = '-' + ans
        l = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        ans = '0' * (l.index(date[1])+1 < 10) + str(l.index(date[1])+1) + ans
        ans = '-' + ans
        ans = str(date[2]) + ans
        return ans