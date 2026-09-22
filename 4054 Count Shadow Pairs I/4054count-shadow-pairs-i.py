class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        stack = []
        answer = stack_sum = 0
        for i in nums:
            curr = 1
            while stack and stack[-1][0] >= i:
                last_n, count = stack.pop()
                if last_n == i:
                    curr += count
                stack_sum -= count
            answer += stack_sum
            stack_sum += curr
            stack.append((i, curr))
        return answer