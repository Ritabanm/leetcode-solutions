class Solution:
    def removeSubstring(self, s: str, k: int) -> str:

        left, total, balStrLen = 0, 0, k + k
        ans, buffer = [], deque()

        for ch in s:
            if ch == '(':
                if left == total:
                    buffer.append("(")
                    left+= 1
                    total+= 1
                else:
                    ans.append(buffer)
                    left, total, buffer = 1, 1, ["("]

            else:
                buffer.append(")")
                total+= 1
                if left >= k and total - left == k:
                    left-= k
                    total-= balStrLen

                    for ch in range(balStrLen):
                        buffer.pop()
 
                    if ans and left == 0:
                        buffer = ans.pop()
                        left, total = buffer.count("("), len(buffer)

        ans.append(buffer)
        return ''.join(chain(*ans))