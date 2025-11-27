class Solution:
    def componentValue(self, nums, edges):
        if not edges:
            return 0

        n, dict1, result = len(nums), defaultdict(list), sum(nums)

        for i,j in edges:
            dict1[i].append(j)
            dict1[j].append(i)

        def function(node,parent,i):
            total = nums[node]

            for neighbor in dict1[node]:
                if neighbor != parent:
                    total += function(neighbor,node,i)

            return total if total != i else 0

        for i in range(max(nums),result//min(nums)):
            if result%i == 0 and function(0,-1,i) == 0:
                return result//i - 1

        return 0