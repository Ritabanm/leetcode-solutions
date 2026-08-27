class Solution:
    def findGoodIntegers(self, n):
        dict1 = defaultdict(set)

        for i in range(1,int(pow(n,1/3))+1):
            for j in range(1,int(pow(n,1/3))+1):
                if i**3 + j**3 <= n and i <= j:
                    dict1[i**3+j**3].add((i,j))

        result = []

        for key,val in dict1.items():
            if len(val) >= 2:
                result.append(key)

        return sorted(result)