class Solution:
    def validSubarrays(self, A, k):
        peak = [i for i in range(1, len(A) - 1) if A[i] > A[i-1] and A[i] > A[i + 1]]
        P, res = len(peak), 0
        for i, p in enumerate(peak):
            prev = max(peak[i-1] + 1 if i > 0 else 0, p-k)
            nxt = min(peak[i + 1] - 1 if i + 1 < P else len(A) - 1, p + k)
            res += (p - prev + 1) * (nxt - p + 1)
        return res