class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        map = {}
        res = 0

        for x in nums:
            map2 = {}
            for y in map:
                map2[y & x] = map2.get(y & x, 0) + map[y]
            map2[x] = map2.get(x, 0) + 1
            map = map2
            res += map.get(k, 0)

        return res