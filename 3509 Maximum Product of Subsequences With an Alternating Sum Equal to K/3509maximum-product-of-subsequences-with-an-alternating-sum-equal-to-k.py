class Solution:
    def maxProduct(self, A: List[int], k: int, limit: int) -> int:
        pos, neg = defaultdict(set), defaultdict(set)
        for a in A:
            pos2 = {s - a: {p * a for p in neg[s] if p * a <= limit} for s in neg}
            neg2 = {s + a: {p * a for p in pos[s] if p * a <= limit} for s in pos}
            for s in pos2:
                pos[s] |= pos2[s] if a else {0}
            for s in neg2:
                neg[s] |= neg2[s] if a else {0}
            if a <= limit:
                neg[a].add(a)
        return max(res) if (res := pos[k] | neg[k]) else -1