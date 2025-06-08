class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        prev = 0
        for elem in nums:
            if elem == prev:
                continue

            cnt = elem - prev - 1
            cnt_to_add = min(cnt, k)
            result += cnt_to_add * (prev + 1 + prev + cnt_to_add) // 2
            k -= cnt_to_add
            if k == 0:
                break
            prev = elem
        
        if k > 0:
            result += k * (prev + 1 + prev + k) // 2
        
        return result