class Solution:
    def canMakeEqual(self, A: List[int], k: int) -> bool:
        def test(v):
            ind = [i for i, a in enumerate(A) if a == v]
            return len(ind) % 2 == 0 and sum(ind[1::2]) - sum(ind[::2]) <= k
        return test(1) or test(-1)