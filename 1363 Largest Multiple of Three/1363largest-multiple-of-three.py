class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        buket, total = [[],[],[]], 0
        for i in digits:
            buket[i % 3].append(i)
            total += i
        r = total % 3
        if r:
            if buket[r]:
                buket[r].pop()
            elif len(buket[-r]) > 1:
                buket[-r].pop() 
                buket[-r].pop() 
        res = []
        res += buket[0] + buket[1] + buket[2]
        res.sort(reverse=True)
        if len(res) == 0:
            return ""
        if res[0] == 0:
            return "0"
        return "".join(str(i) for i in res)