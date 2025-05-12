class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []
        for i, num in enumerate(nums):
            if num:
                self.nums.append((i,num))  

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        i = j = 0

        while i<len(self.nums) and j<len(vec.nums):
            i_idx, i_num  = self.nums[i]
            j_idx, j_num = vec.nums[j]
            if i_idx == j_idx: 
                dot_product += (i_num*j_num)
                i+=1
                j+=1
            elif i_idx > j_idx:
                j+=1

            else:
                i+=1
        return dot_product


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)