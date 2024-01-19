class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        N = len(arr)
        lookup = defaultdict(list)
        for i in range(k):
            j = i
            while j < N:
                lookup[j % k].append(arr[j])
                j += k

        total = 0
        for key in lookup.keys():
            A = lookup[key]
            if len(A) == 1:
                continue

            nums = [A[0]]
            for x in A[1:]:
                index = bisect_right(nums, x)

                if index == len(nums):
                    nums.append(x)

                nums[index] = x

            total += len(A) - len(nums)

                

        return total



            

            

        
        