class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        b = target[0]
        res = 0 if b=="0" else 1
        for i in target:
            if(i != b):
                res += 1
                b = i
                
        return res