class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        answer = []

        min_pair_diff = float('inf')
        for i in range(len(arr)-1):
            min_pair_diff = min(min_pair_diff, arr[i+1]-arr[i])
        
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == min_pair_diff:
                answer.append([arr[i], arr[i+1]])
        return answer