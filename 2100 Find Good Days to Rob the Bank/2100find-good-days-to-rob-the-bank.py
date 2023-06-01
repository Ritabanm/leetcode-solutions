class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N = len(security)
        if time == 0:
            return [i for i in range(N)]
        
        """
        example: [5,3,3,3,5,6,2]
        non_increasing_counts = [0, 1, 2, 3, 0, 0, 1]
        non_decreasing_counts = [0, 4, 3, 2, 1, 0, 0]
        """

        non_increasing_counts = [0] * N
        non_decreasing_counts = [0] * N
        # recording the days **before**, so we accumulate the count from the start
        for i in range(1, N):
            if security[i] <= security[i - 1]:
                non_increasing_counts[i] = non_increasing_counts[i - 1] + 1

        # recording the days **after**, so we accumulate the count from the end
        for i in range(N - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_decreasing_counts[i] = non_decreasing_counts[i + 1] + 1
        
        res = []
        for i in range(N):
            if non_increasing_counts[i] >= time and non_decreasing_counts[i] >= time:
                res.append(i)

        return res