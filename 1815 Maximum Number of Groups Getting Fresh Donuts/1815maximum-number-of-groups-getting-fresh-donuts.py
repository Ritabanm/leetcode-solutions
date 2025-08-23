class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        
        @functools.lru_cache(None)
        def helper(rem, used):
            if used == target:
                return 0
            seen = set()
            best = 0
            for i in range(len(groups)):
                if not (bitmask[i] & used):
                    if groups[i] not in seen:
                        seen.add(groups[i])
                        r = (rem + groups[i]) % batchSize
                        best = max(best, helper(r, used | bitmask[i]))
                        if r == 0:
                            return int(rem == 0) + best
            return int(rem == 0) + best
        
        # 1. Greedily serve all groups that are a multiple of batchSize first.
        new_groups = [g%batchSize for g in groups]
        res = len(groups) - len(new_groups)
        groups = new_groups
        
        # 2. Greedily serve all pairs of groups where group1 + group2 is a multiple of batchsize.
        count = collections.defaultdict(int)
        for g in groups:
            target = batchSize - g
            if count[target]:
                count[target] -= 1
                res += 1
            else:
                count[g] += 1
        
        # 3. Use top-down DP to find the optimal configuration of the remaining groups.        
        groups = sum([[i]*count[i] for i in count], [])
        target = (1 << len(groups)) - 1
        bitmask = [1 << i for i in range(len(groups))]
        return res + helper(0, 0)