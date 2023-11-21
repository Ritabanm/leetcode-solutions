class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        # normalize x and y so x > y
        x, y = max(x, y), min(x, y)

        def check_nums(num_steps):
            """
            check if we can get everything <0 in num_steps
            invariant: y < x
            """

            # because x > y, each operation removes y from all numbers and an additional (x-y) from 1 number
            baseline = y * num_steps

            # we now need to figure out how x should have been allocated
            # because we are taking num_steps that implies that x was allocated num_steps times
            # this variable will keep track of the number of x allocations we have available
            x_bank = num_steps

            # for each number, we subtract the baseline
            # if the residual is greater than 0, we know that it needed to have x subtracted from it
            # in order to be <=0 in num_steps
            # the number of x allocations it needed was math.ceil(residual / (x - y))
            # we can do this so long as x_bank is positive
            for n in nums: 
                residual = n - baseline
                if residual > 0:
                    x_bank -= math.ceil(residual / (x - y))
                
                    if x_bank < 0:
                        return False

            return True


        # regular binary search
        l = 0
        r = max(nums) // min(x, y) + 1
        last_acceptable = -1

        while l <= r:
            m = l + (r-l)//2

            acceptable = check_nums(m)
            if acceptable:
                r = m - 1
                last_acceptable = m
            else:
                l = m + 1

        return last_acceptable