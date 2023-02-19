class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offerEnd = defaultdict(list)

        for start, end , gold in offers:
            offerEnd[end].append((start, gold))

        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = dp[i-1]
            for start, gold in offerEnd[i-1]:
                dp[i] = max(dp[i], dp[start]+gold)
        
        return dp[n]