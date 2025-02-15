class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)

        for i in range(n):
            ele = nums[i]

            if ele < a:
                flag = "L"
            elif a <= ele <= b:
                flag = "M"
            else:
                flag = "R"

            nums[i] = flag

        countL = 0
        passR = {}
        for i in range(n - 1, -1, -1):
            if nums[i] == "L": countL += 1

            if nums[i] == "R":
                passR[i] = countL

        stepsL = 0
        factor = 0

        for i in range(n):
            if nums[i] == "L":
                stepsL += i - factor
                factor+=1

        stepsR = 0
        factor = n - 1

        for i in range(n):
            if nums[i] == "R":
                new_position = i + passR[i]
                stepsR += factor - new_position
                factor-=1

        return (stepsL + stepsR) % (7 + 10**9)

        