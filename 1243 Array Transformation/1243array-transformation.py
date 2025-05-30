class Solution:
    def arrayMatch(arr1, arr2):
        for i, el in enumerate(arr1):
            if el != arr2[i]:
                return False
        return True

    def transformArray(self, arr: List[int]) -> List[int]:
        while 1:
            res = []
            for i, el in enumerate(arr):
                if i == 0 or i == len(arr) - 1:
                    res.append(el)
                else:
                    if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                        res.append(el + 1)
                    elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                        res.append(el - 1)
                    else:
                        res.append(el)
                        
            if Solution.arrayMatch(arr, res):
                return res
            arr = res
