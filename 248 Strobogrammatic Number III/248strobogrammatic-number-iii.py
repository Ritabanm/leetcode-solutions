class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        low_n, high_n = int(low), int(high)
        def dfs(low, high, length, path):
            if len(path) > length: return 
            if len(path) == length:
                if len(path) != 1 and path[0] == '0': return 
                else:
                    if int(path) >= low_n and int(path) <= high_n:
                        self.res += 1
                    return 
            dfs(low, high, length, '0'+path+'0')
            dfs(low, high, length, '6'+path+'9')
            dfs(low, high, length, '9'+path+'6')
            dfs(low, high, length, '8'+path+'8')
            dfs(low, high, length, '1'+path+'1')
        self.res = 0
        for length in range(len(low), len(high)+1):
            dfs(low, high, length, "")
            dfs(low, high, length, "1")
            dfs(low, high, length, "8")
            dfs(low, high, length, "0")
        return self.res
        