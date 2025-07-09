class Solution:
    

    def __init__(self):
        self.count = 0

    def rand10(self):
        """
        :rtype: int
        """
        res = (self.count + rand7())
        self.count+=1
        if res>10:
            res = (res%10)+1
        return res
        