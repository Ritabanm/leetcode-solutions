class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        mapp = defaultdict(set)
        ans = 0
        last = None
        for i in nums:
            if i==last:
                continue
            b = format(i,'b').count('1')
            mapp[b].add(i)
            t = k-b
            for j in range(max(0,t),31):
                ans+=len(mapp[j])*2
                if i in mapp[j]:
                    ans-=1
            last = i
        return ans