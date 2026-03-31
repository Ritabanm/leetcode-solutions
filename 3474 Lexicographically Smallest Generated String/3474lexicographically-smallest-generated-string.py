class Solution:
    def generateString(self, A: str, B: str) -> str:
        """
        Greedy
        """
        m, n = len(A), len(B)
        ans = [""] * (m + n - 1)
        T = [False] * (m + n - 1)

        # 1. fill all the `T`s
        for i in range(m):
            if A[i] == "T":
                for j in range(n):
                    if ans[i + j] and ans[i + j] != B[j]:
                        return ""
                    ans[i + j] = B[j]
                    T[i + j] = True

        # 2. fill all the `F`s with 'a' first
        for i in range(m + n - 1):
            if not ans[i]:
                ans[i] = "a"

        for i in range(m):
            if A[i] == "F":
                # 3. check if aleady different
                diff = False
                for j in range(n):
                    if ans[i + j] != B[j]:
                        diff = True
                        break
                if diff:
                    continue

                # 4. find a char to change from the end to the begin
                change = False
                for j in range(n - 1, -1, -1):
                    if T[i + j] or ans[i + j] == "z":
                        # if cur is `T` or "z", it cannot be changed, continue
                        continue

                    ans[i + j] = chr(ord(ans[i + j]) + 1)
                    change = True
                    break

                if not change:
                    # cannot change, return
                    return ""

        return "".join(ans)