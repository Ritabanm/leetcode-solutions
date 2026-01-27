class Solution:
    def minUnlockedIndices(self, nums: List[int], locked: List[int]) -> int:

        nums = ''.join(map(str,nums))       # nums to string

        last1 = nums.rfind('1')
        init2, last2 = nums.find('2'), nums.rfind('2')
        init3 = nums.find('3')
                                            # Hint 3
        if last1 > init3 >= 0: return -1
        if last2 == -1: return 0
                                            # Hints 1 and 2
        return (sum(locked[init2: last1]) * (last1 != -1)
              + sum(locked[init3: last2]) * (init3 != -1))