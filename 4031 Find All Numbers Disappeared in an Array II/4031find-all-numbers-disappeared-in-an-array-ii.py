class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums = set(nums)
        answer = []
        start = lower
        while lower <= upper:
            if lower in nums:
                lower+=1
            else:
                first = lower
                while lower not in nums and lower <= upper:
                    lower+=1
                answer.append([first,lower-1])
        return answer
         

        