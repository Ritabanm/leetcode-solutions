class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        #[position, range]
        d = defaultdict(int)
        sr = sorted(list(set(requirement)))
        myset = set()
        orig = [0] * n
        print(sr)
        for l in lights:
            val = l[1]
            left = max(0, l[0] - l[1])
            right = min(n - 1, l[0] + l[1])
            print(left, right)
            if left >= 0:
                orig[left] += 1
            if right + 1 < len(orig): 
                orig[right + 1] -= 1
        print(orig)
        a = list(itertools.accumulate(orig))
        print(a)
        res = 0
        for i, val in enumerate(a):
            if val >= requirement[i]:
                res += 1
        return res

            
            



        