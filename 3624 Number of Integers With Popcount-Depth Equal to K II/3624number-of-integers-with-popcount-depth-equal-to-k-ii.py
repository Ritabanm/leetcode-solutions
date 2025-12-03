class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        d = defaultdict(SortedSet)
        def depth(num):
            if num == 1: return 0
            return 1 + depth(num.bit_count())
        for i, num in enumerate(nums):
            d[depth(num)].add(i)
        ans = []
        for query in queries:
            if query[0] == 1:
                l, r, k = query[1:]
                ans.append(d[k].bisect_right(r) - d[k].bisect_left(l))
            else:
                id, val = query[1:]
                d[depth(nums[id])].remove(id)
                nums[id] = val
                d[depth(val)].add(id)
        return ans