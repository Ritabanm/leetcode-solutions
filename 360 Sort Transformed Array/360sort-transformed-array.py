class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        answer = []
        for num in nums:
            answer.append((a*num*num) + (b*num)+c)
        
        answer.sort()
        return answer