class Solution:
    def permute(self, n: int) -> List[List[int]]:
        def s(temp, v, l):
            if len(temp)==n:
                ans.append(temp.copy())
                return 
            if v==0:
                for i in even:
                    if i not in l:
                        temp.append(i)
                        l.add(i)
                        s(temp,1, l)
                        l.remove(i)
                        temp.pop()
            else:
                for i in odd:
                    if i not in l:
                        temp.append(i)
                        l.add(i)
                        s(temp, 0, l)
                        l.remove(i)
                        temp.pop()
        ans = []
        odd = set()
        even = set()
        for i in range(1, n+1):
            if i%2==1:
                odd.add(i)
            else:
                even.add(i)
        l = set()
        s([], 0, l)
        s([], 1, l)
        return sorted(ans)