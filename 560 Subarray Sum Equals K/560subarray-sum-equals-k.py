"""class Solution:
    def subarraySum(self, nums, k):
        dic = defaultdict(int)
        dic[0]=1
        runsum=0
        count=0
        for num in nums:
            runsum+=num
            diff = runsum-k
            if diff in dic:
                count+=dic[diff]
            dic[runsum]+=1
        return count
"""

class Solution:
    def subarraySum(self, nums, k):
        dic = defaultdict(int)
        dic[0]=1
        runsum = 0
        count = 0
        for num in nums:
            runsum+=num
            diff = runsum-k
            if diff in dic:
                count+=dic[diff]
            dic[runsum]+=1
        return count