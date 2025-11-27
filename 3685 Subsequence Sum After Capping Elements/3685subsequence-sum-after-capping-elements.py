from typing import List

class Solution:
    def subsequenceSumAfterCapping(self, arr: List[int], k: int) -> List[bool]:
        n = len(arr)
        arr.sort() 

        sum_possible = [False] * (k + 1)
        sum_possible[0] = True  


        ans = [False] * n

        i = 0 
        for x in range(1, n + 1):
            while i < n and arr[i] < x:
                for j in range(k, arr[i] - 1, -1):
                    if sum_possible[j - arr[i]]:
                        sum_possible[j] = True
                i += 1

            bigger = n - i


            for count in range(0, bigger + 1):
                total_from_x = count * x
                if total_from_x > k:
                    break 
                remainder = k - total_from_x
                if sum_possible[remainder]:
                    ans[x - 1] = True
                    break

        return ans