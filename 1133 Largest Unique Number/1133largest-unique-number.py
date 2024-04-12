class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        freq_map = {}
        for num in nums:
            freq_map[num]=freq_map.get(num,0)+1
        
        #Sorted orderedDict.
        sorted_map = OrderedDict(sorted(freq_map.items(), reverse = True))

        #largest num.
        for num, freq in sorted_map.items():
            if freq ==1:
                return num
        return -1