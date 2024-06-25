class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        r = float('inf')
        count = 0
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff == r:
                count += 1
            else:
                count -= 1
            if count < 0: 
                r = diff 
                count = 0
        for i in range(1, len(arr)):
            prev = arr[i - 1]
            if prev + r != arr[i]:
                return prev + r
        
        if r == 0 : return arr[0] + r