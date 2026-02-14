class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(current):
            if current > n:
                return  # Stop if the number exceeds n
            result.append(current)  # Add the number to the result
            for i in range(10):  # Explore children (e.g., 10, 11, 12, ...)
                next_num = current * 10 + i
                if next_num > n:
                    break  # Stop exploring further if it exceeds n
                dfs(next_num)

        for i in range(1, 10):  # Start with root numbers (1 to 9)
            dfs(i)

        return result