class Solution:
    def reformatNumber(self, number: str) -> str:
        store = list(filter(lambda x: x.isdigit(), number))
        leng = len(store)
        res = ''
        
        for i in range(0, leng, 3):
            if leng - i == 4:
                res += ''.join(store[i:i+2]) +'-'+ ''.join(store[i+2:])
                break
            else:
                res += ''.join(store[i:i+3]) + '-'
        res = res.rstrip('-')
        return res
            