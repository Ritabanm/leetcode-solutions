class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        size = len(num)
        self.result = None

        def dfs(start, path):
            if len(path) > 2 and path[-3] + path[-2] != path[-1]:
                return False
            if start == size:
                if len(path) > 2 and self.result is None:
                    self.result = path.copy()
                    return True
                return False
            for i in range(start, size):
                if num[start] == "0" and i > start:
                    break
                if int(num[start : i + 1]) > (2**31):
                    break
                path.append(int(num[start : i + 1]))
                if dfs(i + 1, path):
                    return True
                path.pop()
            return False

        dfs(0, [])
        return self.result if self.result is not None else []