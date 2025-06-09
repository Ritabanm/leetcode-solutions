
class Solution:
    def findMaximumLength(self, A: List[int]) -> int:
        n = len(A)
        if n == 1: return 1
        prefix_sum = list(accumulate(A))
        dq, cur, r = deque(), 0, 0  
        for i in range(n):
            while dq and dq[0][0] <= prefix_sum[i]:
                (_, r, cur) = dq.popleft()
            minv = 2*prefix_sum[i] - cur
            while dq and dq[-1][0] >= minv: 
                dq.pop()
            dq.append((minv, r+1, prefix_sum[i]))
        return r+1

    
    

   