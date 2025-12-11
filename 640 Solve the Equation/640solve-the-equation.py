class Solution:
    def solveEquation(self, equation: str) -> str:
        sum_coefs, sum_nums = 0, 0
        sign, side = 1, 1
        value = ''
        for i, char in enumerate(equation):
            if char in ('+', '-', '=') or i == len(equation) - 1:
                if i == len(equation) - 1:
                    value += char
                if value != '':
                    if 'x' in value:
                        sum_coefs += sign * side * \
                            (1 if value == 'x' else int(value.replace('x', '')))
                    else:
                        sum_nums += sign * side * int(value)
                if char == '=':
                    sign, side = 1, -1
                elif char in ('+', '-'):
                    sign= 1 if char =='+' else -1
                value = ''
            else:
                value += char
        if sum_coefs == 0:
            if sum_nums == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return f'x={-sum_nums // sum_coefs}'