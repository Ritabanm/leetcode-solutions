class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        ans , heap = 0, []
        for bit, score in zip(s, nums):
            if bit=="1":
                ans-= heappushpop(heap, -score)
            else:
                heappush(heap,-score)
        return ans