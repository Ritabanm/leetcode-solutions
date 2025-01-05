class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = defaultdict(list)
        
        # Step 1: Group elements by their diagonal index (i + j)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonal_map[i + j].append(nums[i][j])
        
        # Step 2: Traverse the dictionary keys in sorted order
        result = []
        for diagonal_index in sorted(diagonal_map.keys()):
            # Reverse the order of elements for the current diagonal
            result.extend(reversed(diagonal_map[diagonal_index]))
        
        return result
