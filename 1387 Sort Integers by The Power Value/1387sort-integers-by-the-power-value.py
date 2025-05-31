class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        sl = SortedList()
        def f(num, cnt, orig):
            if num == 1:
                #print(orig, cnt)
                sl.add((cnt, orig))
                return cnt
            if num == 1:
                return cnt
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            f(num, cnt + 1, orig)

        for i in range(lo, hi + 1):
            num = i
            cnt = 0
            orig = i
            f(num, cnt, orig)
            #print(num, res)
        print(sl)
        return sl[k - 1][1]

