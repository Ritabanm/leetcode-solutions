class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for i, dis in lights:
            d[i-dis] += 1                             # index at left-end starts covering
            d[i+dis+1] -= 1                           # next index of right-end stops covering
        cur, max_idx, max_val = 0, -1, -sys.maxsize
        for idx, val in sorted(d.items()):            # sort by key would be sufficient
            cur += val
            if cur > max_val:                         # count maximum brightness
                max_val, max_idx = cur, idx
        return max_idx