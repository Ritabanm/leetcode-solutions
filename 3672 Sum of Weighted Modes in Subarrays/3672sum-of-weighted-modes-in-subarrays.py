class Solution:
    def modeWeight(self, nums, k):
        from sortedcontainers import SortedList 

        n, total = len(nums), 0

        result, dict1 = SortedList(), defaultdict(int)

        for i in range(k):
            dict1[nums[i]] += 1 

        for key,val in dict1.items():
            result.add((-val,key))

        total += abs(result[0][0])*result[0][1]

        for i in range(k,n):
            if nums[i] not in dict1:
                result.add((-1,nums[i]))
            else:
                result.remove((-dict1[nums[i]],nums[i]))
                result.add((-dict1[nums[i]]-1,nums[i]))

            dict1[nums[i]] += 1 
            dict1[nums[i-k]] -= 1 

            if dict1[nums[i-k]] == 0:
                del dict1[nums[i-k]]

            if nums[i-k] not in dict1:
                result.remove((-1,nums[i-k]))
            else:
                if (-(dict1[nums[i-k]]+1),nums[i-k]) in result:
                    result.remove((-(dict1[nums[i-k]]+1),nums[i-k]))
                    result.add((-dict1[nums[i-k]],nums[i-k]))

            total += abs(result[0][0])*result[0][1]
            
        return total