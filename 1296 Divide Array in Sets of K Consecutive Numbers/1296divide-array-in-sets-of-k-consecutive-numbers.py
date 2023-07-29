class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()

        dictionary = defaultdict(int)
        count = 0
        length = len(nums)

        if len(nums) % k != 0:
            return False

        for num in nums:
            dictionary[num] += 1
        
        for num in nums:
            if dictionary[num] > 0:  # Start of a new sequence
                for curr in range(num, num + k):  # Attempt to form a sequence of length k
                    if dictionary[curr] == 0:
                        return False  # Cannot form a sequence
                    dictionary[curr] -= 1  # Use this number

        return True
            
            
                    

