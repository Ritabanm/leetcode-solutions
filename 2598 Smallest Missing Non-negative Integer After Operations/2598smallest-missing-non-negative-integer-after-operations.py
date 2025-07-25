class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        ctr = Counter(map(lambda x: x%value,nums))  # <––  1.

        mn = min((n for n in range(value)),         # <––  2.
                  key = lambda x: (ctr[x],x))       #
        
        return  mn+value*ctr[mn]                    # <––  3.