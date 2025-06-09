class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
            d = defaultdict(set)
            for ids, times in logs:
                d[ids].add(times)
            res = [0 for _ in range(k)]
            d = Counter(len(d[i]) for i in d)
            for i in d:
                res[i - 1] = d[i]
            
            return res