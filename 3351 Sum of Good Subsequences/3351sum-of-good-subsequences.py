class Solution:
  def sumOfGoodSubsequences(self, nums: List[int]) -> int:
    total_sum, total_cnt, mod = defaultdict(int), defaultdict(int), 10**9 + 7
    for v in nums:
      tmp_sum = (total_sum[v - 1] + total_sum[v + 1]) % mod
      tmp_cnt = (total_cnt[v - 1] + total_cnt[v + 1]) % mod
      total_cnt[v] += + tmp_cnt + 1
      total_sum[v] += + tmp_sum + v * (tmp_cnt + 1)

    return sum(total_sum.values()) % mod