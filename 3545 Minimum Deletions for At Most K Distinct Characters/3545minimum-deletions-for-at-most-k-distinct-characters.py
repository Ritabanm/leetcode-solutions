class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = Counter(s)
        if len(freq)<=k:
            return 0

        freq_counts = sorted(freq.values())
        to_remove = len(freq)-k
        deletions = sum(freq_counts[:to_remove])
        return deletions