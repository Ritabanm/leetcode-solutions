class Solution:
    def findKthPositive(self, arr, k):
        for num in arr:
            if num<=k:
                k+=1
            elif num>k:
                break
        return k