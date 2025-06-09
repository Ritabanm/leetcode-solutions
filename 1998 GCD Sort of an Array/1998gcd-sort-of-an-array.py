class Solution:
    def gcdSort(self, nums):
        dict1 = {}

        def find(x):
            if x not in dict1:
                return x 
            else:
                if x != dict1[x]:
                    dict1[x] = find(dict1[x])
                return dict1[x]

        def union(x,y):
            a, b = find(x), find(y)

            if a != b:
                dict1[b] = a 

        for i in nums:
            for j in range(2,int(math.sqrt(i))+1):
                if i%j == 0:
                    union(i,j)
                    union(i,i//j)

        for i,j in zip(nums,sorted(nums)):
            if find(i) != find(j):
                return False 

        return True  