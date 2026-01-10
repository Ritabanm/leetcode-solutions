class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(i, k):
            if k==0:
                return 0
            
            if k<(1<<i):
                return dfs(i-1,k)
            
            else:
                return dfs(i-1,k-(1<<i))+operations[i]
            
        depth = floor(log2(k-1)) if k>1 else 0

        dig = dfs(depth, k-1)
        return chr(ord('a')+dig%26)