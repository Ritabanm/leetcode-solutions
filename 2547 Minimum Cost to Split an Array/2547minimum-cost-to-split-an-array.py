# from functools import lru_cache

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        trimmed_subarray_lengths = {}

        seen_more = set()
        seen_once = set()

        for i in range(len(nums)):
            seen_more.clear()
            seen_once.clear()
            for j in range(i, len(nums)):
                if nums[j] not in seen_more:
                    if nums[j] in seen_once:
                        seen_once.remove(nums[j])
                        seen_more.add(nums[j])
                    else:
                        seen_once.add(nums[j])

                total_length = (j - i) + 1
                trimmed_subarray_lengths[(i, j)] = total_length - len(seen_once)
        
        answer = [float('inf') for _ in range(len(nums))]

        for i in reversed(range(len(nums))):
            for j in range(len(nums) - 1, i - 1, -1):
                next_answer = answer[j + 1] if j + 1 < len(nums) else 0
                answer[i] = min(
                    answer[i],
                    trimmed_subarray_lengths[(i, j)] + k + next_answer
                )
        
        return answer[0]