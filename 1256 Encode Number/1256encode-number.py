class Solution:
    def encode(self, num: int) -> str:
        res = ''
        num += 1

        while(num):
            res = ('1' if num&1 else '0') + res
            num >>= 1
        return res[1:]