class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        l = len(A)
        for i in range (l-1, -1, -1):
            A[i] += K
            K = (A[i] - A[i] % 10) // 10
            A[i] = A[i] % 10
        if K: A = [int(x) for x in str(K)] + A
        return A