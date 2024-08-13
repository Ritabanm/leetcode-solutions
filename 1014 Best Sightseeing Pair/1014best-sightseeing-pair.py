class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxScore = 0
        maxValueSoFar = values[0]  # Initialize with the first spot's value + index

        for j in range(1, len(values)):
            # Calculate the score for the current index j
            maxScore = max(maxScore, maxValueSoFar + values[j] - j)
            # Update maxValueSoFar for future iterations
            maxValueSoFar = max(maxValueSoFar, values[j] + j)
        
        return maxScore