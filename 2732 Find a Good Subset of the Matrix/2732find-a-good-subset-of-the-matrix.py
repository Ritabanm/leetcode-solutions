class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        # bitmask
        ls = []
        for i in range(len(grid)):
            bitmask = 0
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    bitmask |= 1<<j
            ls.append(bitmask)
            if bitmask == 0:
                return [i]

        # need to find ls[i] and ls[j] where ls[i] & ls[j] == 0
        # there are 2^5 maximum bitmask
        st_ls = list(set(ls))
        # print(st_ls)
        t1, t2 = -1, -1
        for i in range(len(st_ls)):
            for j in range(i+1, len(st_ls)):
                if st_ls[i] & st_ls[j] == 0:
                    t1 = st_ls[i]
                    t2 = st_ls[j]
                    break
        if t1 == -1 and t2 == -1:
            return []
        else:
            ans = []
            for i in range(len(ls)):
                if ls[i] == t1:
                    ans.append(i)
                    break
            for j in range(len(ls)):
                if ls[j] == t2:
                    ans.append(j)
                    break
            return sorted(ans)