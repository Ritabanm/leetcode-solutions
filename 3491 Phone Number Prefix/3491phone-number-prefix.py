class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        sorted_numbers = sorted(numbers)
        prev = 'None'

        # print(sorted_numbers)
        for each_number in sorted_numbers:
            pattern = f'^{prev}.*'
            if re.match(pattern, each_number):
                return False
            prev = each_number
        return True