class Solution:
    def minOperations(self, k: int) -> int:
        return ceil(sqrt(k)) -1 + k //ceil(sqrt(k)) - (k%ceil(sqrt(k))==0)