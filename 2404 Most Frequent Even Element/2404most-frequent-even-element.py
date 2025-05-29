class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        #Filter Even numbers
        listz = [i for i in nums if i%2==0]
        if not listz:
            return -1
        
        a = Counter(listz)
        k = float('-inf')
        l = float('inf')

        for n,m in a.items():
            if m>k or (m==k and n<l):
                k=m
                l = n
        return l