class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        seen=set()
        for i in range(len(nums)):
            if i not in seen:
                local=set()
                while True:
                    if i in local:
                        return True
                    if i in seen:
                        break
                    local.add(i)
                    seen.add(i)
                    prev=i
                    i=(i+nums[i])%len(nums)
                    if prev==i or (nums[i]>0)!=(nums[prev]>0):
                        break     
        return False      