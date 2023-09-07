class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        result = ''

        for x in range(9, -1, -1):
            if num >= 16 ** x:
                div = num // (16 ** x)

                if div > 9:
                    div = chr(ord('A') + (div - 10))
                elif div > 1:
                    return 'ERROR'
                elif div == 1:
                    div = 'I'
                elif div == 0:
                    div = 'O'

                result += div
                num -= (16 ** x) * (num // (16 ** x))

            elif result:
                result += 'O'
        
        return result