class Solution:
    def topKFrequent(self,nums,k):
        group = {}
        for num in nums:
            if num in group:
                group[num]+=1
            else:
                group[num]=1
        bucket = [[] for _ in range(len(nums)+1)]

        for num, count in group.items():
            bucket[count].append(num)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res

