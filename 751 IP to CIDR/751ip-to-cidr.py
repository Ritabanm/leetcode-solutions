class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        '''
        block_size = 2^(32-k)
        k = 32 - log2(block_size)
        '''
        def to_int(ip_address):
            a, b, c, d = ip_address.split('.')
            return (int(a) << 24) | (int(b) << 16) | (int(c) << 8) | (int(d))
        
        def to_ip(x):
            return f"{x>>24 & 255}.{x>>16 & 255}.{x>>8 & 255}.{x & 255}"

        def highest_pow_of_two(x):
            return 1 << (x.bit_length() - 1)

        res = []
        x = to_int(ip)
        remain = n

        while remain > 0:
            low_bit = (x & -x) or (1 << 32)          # handles x == 0
            fit = highest_pow_of_two(remain)
            block = min(low_bit, fit)
            k = 32 - int(math.log2(block))
            res.append(to_ip(x) + '/' + str(k))
            x += block
            remain -= block
        return res