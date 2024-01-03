class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
    
        # Check if the input list is empty
        if nums == []:
            return []
        
        # Initialize the list to store the summary ranges
        ranges = []
        
        # Initialize variables for the start and end of the range
        start = nums[0]
        end = nums[0]

        # Iterate through the numbers starting from the second element
        for num in nums[1:]:
            if num == end + 1:
                # The number is consecutive, update the end of the range
                end = num
            else:
                # The number is not consecutive, add the current range to the result list
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
                
                # Reset the start and end to the current number
                start = num
                end = num

        # Add the last range to the result list
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")
        
        return ranges