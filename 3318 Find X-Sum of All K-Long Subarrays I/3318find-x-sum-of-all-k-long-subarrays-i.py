class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        h = Counter(nums[:k])
        res = []

        def sum_x(i):
            if len(h)<=x:
                return sum(nums[i:k+i])

            freq = [(j,i) for i,j in h.items()]
            freq.sort(reverse=True)

            return sum(freq[i][0]*freq[i][1] for i in range(x))

        res.append(sum_x(0))

        for i in range(len(nums)-k):
            h[nums[i]]-=1
            h[nums[i+k]]+=1
            res.append(sum_x(i+1))   
        return res


