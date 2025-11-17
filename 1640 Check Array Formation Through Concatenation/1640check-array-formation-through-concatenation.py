class Solution:
    def canFormArray(self, arr, pieces):
        n = len(arr)
        i = 0
        while i<n:
            for p in pieces:
                if p[0]==arr[i]:
                    break
            else:
                return False
            for x in p:
                if x!=arr[i]:
                    return False
                i+=1
        return True