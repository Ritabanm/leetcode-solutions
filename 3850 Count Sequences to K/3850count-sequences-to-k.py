from math import gcd
from collections import defaultdict

class Solution:
    def countSequences(self, nums, k):
        prev = defaultdict(int)
        prev[(1,1)]=1
        for x in nums:
            nw = defaultdict(int)
            for (num, den), ways in prev.items():
                nw[(num, den)]+=ways
                g = gcd(x,den)
                nnum=num*(x//g)
                nden = den//g
                nw[(nnum, nden)]+=ways

                g = gcd(x, num)
                nnum = num//g
                nden = den*(x//g)
                nw[(nnum,nden)]+=ways
            prev = nw
        ans = 0
        for (num, den), ways in prev.items():
            if num%den==0 and num//den==k:
                ans+=ways
        return ans