class Solution:
    def replaceElements(self, arr):
        Max = arr[-1]
        arr[-1]=-1

        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            arr[i] = Max
            if temp>Max: Max=temp
        return arr