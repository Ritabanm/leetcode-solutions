class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        c = Counter()
        sl = SortedList()
        q = []
        ts = [0] * len(queries)
        for i, (l, r, t) in enumerate(queries):
            q.append((l, r, i))
            ts[i] = t

        block_size = max(1, int(len(nums) / sqrt(len(queries))))

        def mo_cmp(query):
            L, R, idx = query
            block_id = L // block_size
            if block_id % 2 == 0:
                return (block_id, R)
            else:
                return (block_id, -R)

        q.sort(key=mo_cmp)

        currL = 0
        currR = 0

        ans = [0] * len(q)

        def add(pos):
            x = nums[pos]
            if x in c:
                sl.discard((c[x], -x))
            c[x] += 1
            sl.add((c[x], -x))

        def rem(pos):
            x = nums[pos]
            sl.discard((c[x], -x))
            c[x] -= 1
            if c[x] > 0:
                sl.add((c[x], -x))

        for L, R, idx in q:
            while currR <= R:
                add(currR)
                currR += 1

            while currL > L:
                currL -= 1
                add(currL)
            while currR > R + 1:
                currR -= 1
                rem(currR)

            while currL < L:
                rem(currL)
                currL += 1

            if not sl:
                ans[idx] = -1
            else:
                cnt, x = sl[-1]
                if cnt < ts[idx]:
                    ans[idx] = -1
                else:
                    ans[idx] = -x
        return ans