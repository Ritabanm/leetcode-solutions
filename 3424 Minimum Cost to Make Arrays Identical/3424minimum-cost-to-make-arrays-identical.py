class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        if arr == brr:
            return 0
        count_arr = Counter(arr)
        count_brr = Counter(arr)

        count = 0
        for a, b in zip(arr, brr):
            count += abs(a - b)

        with_rearrange = k
        arr.sort()
        brr.sort()
        for a, b in zip(arr, brr):
            with_rearrange += abs(a - b)

        return min(count, with_rearrange)
         
        
            