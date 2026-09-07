class Solution:
    def evenOddBit(self, num):
        binary_num = format(num, 'b')
        
        count_even_bits = len([i for i in range(0, len(binary_num)) if i % 2 == 0 and list(reversed(binary_num))[i] == '1'])
        count_odd_bits = len([i for i in range(0, len(binary_num)) if i % 2 != 0 and list(reversed(binary_num))[i] == '1'])

        return [count_even_bits, count_odd_bits]