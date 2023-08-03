class Solution:
    def delayedCount(self, A: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for e in A:
            hm[e] += 1

        ans = []

        for i in range(k):
            hm[A[i]] -= 1

        for i in range(len(A)):
            if i+k < len(A):
                hm[A[i+k]] -= 1
            ans.append(hm[A[i]])
        
        return ans