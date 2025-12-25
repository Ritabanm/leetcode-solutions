class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)
        buckets = [0] * k

        def backtrack(index):
            if index == len(nums):
                return all(bucket == target for bucket in buckets)
            
            for i in range(k):
                if buckets[i] + nums[index] <= target:
                    buckets[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    buckets[i] -= nums[index]
                if buckets[i] == 0:
                    break
            return False

        return backtrack(0)
