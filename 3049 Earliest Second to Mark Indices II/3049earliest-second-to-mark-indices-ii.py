class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        first_indices = [m] * n  # space: O(n)
        for i, v in enumerate(changeIndices):  # O(m)
            first_indices[v-1] = min(first_indices[v-1], i)
        first_indices = sorted(filter(lambda x: x < m, first_indices))

        left, right = n, min(m + 1, sum(nums) + n + 1)
        res = m + 1
        while left < right:  # O(log(m))
            end = (left + right) // 2
            last_idx = end
            available = 0
            required = sum(nums) + n
    
            used = []  # space: O(n)
            for i in range(bisect.bisect_right(first_indices, end)-1, -1, -1):  # O(n)
                idx = first_indices[i]
                available += last_idx - idx
                last_idx = idx
                v = nums[changeIndices[idx]-1]
                if v < 2:  # there's no difference between 'change 1 to 0' or '1 - 1'
                    pass
                elif available >= 2:
                    required -= v + 1
                    available -= 2
                    heapq.heappush(used, v)  # O(log(n))
                elif used and used[0] < v + 1:
                    required += heapq.heappop(used) - v
                    heapq.heappush(used, v)

            available += last_idx - idx
            if available >= required:
                right = end
                res = min(res, end)
            else:
                left = end + 1

        return res if res < m + 1 else -1