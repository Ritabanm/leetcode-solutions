
class Solution:
    def convertArray(self, nums: List[int]) -> int:
        
        def median(data):
            sorted_data = sorted(data)
            n = len(sorted_data)
            mid = n // 2
            if n % 2 == 0:
                return sorted_data[mid - 1]
            else:
                return sorted_data[mid]

        def find_median_distance(sol_list):
            med = median(sol_list)
            ans =0
            for i in range(len(sol_list)):
                ans+=abs(med- sol_list[i])
            return int(ans)

        def max_increasing_array(nums):
            sol=[]
            for num in nums:
                candidate = [num]
                while len(sol) and median(sol[-1]) > median(candidate):
                    candidate = candidate + sol.pop()
                sol.append(candidate)
            ans=0
            for lis in sol:
                ans+= find_median_distance(lis)
            return ans

        return min(max_increasing_array(nums), max_increasing_array(nums[::-1]))
                