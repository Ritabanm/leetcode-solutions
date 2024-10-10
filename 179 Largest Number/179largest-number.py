from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Convert the numbers to strings
        nums_str = list(map(str, nums))

        # Step 2: Sort the numbers in descending order based on the comparison rule
        nums_str.sort(reverse=True, key=lambda x: x*10)

        # Step 3: Join the sorted strings into the largest number
        largest_num = ''.join(nums_str)

        # Step 4: Handle the edge case where the result might be '0'
        return '0' if largest_num[0] == '0' else largest_num

