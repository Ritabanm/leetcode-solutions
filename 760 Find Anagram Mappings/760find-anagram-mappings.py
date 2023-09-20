class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        hashmap = defaultdict(int) 
        
        for index, val in enumerate(nums2):
            hashmap[val] = index
        
        
        for index, val in enumerate(nums1):
            nums1[index] = hashmap[val]
        
        return nums1