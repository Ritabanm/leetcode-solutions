import math

class Solution:
    def minOperations(self, s):
        n = len(s)
        a = [ord(c) - 97 for c in s]

        def fft(a, invert=False):
            nfft = len(a)

            j = 0
            for i in range(1, nfft):
                bit = nfft >> 1
                while j & bit:
                    j ^= bit
                    bit >>= 1
                j ^= bit

                if i < j:
                    a[i], a[j] = a[j], a[i]

            length = 2
            while length <= nfft:
                ang = 2.0 * math.pi / length
                if invert:
                    ang = -ang

                wlen = complex(math.cos(ang), math.sin(ang))
                half = length >> 1

                for i in range(0, nfft, length):
                    w = 1.0 + 0.0j
                    end = i + half

                    for j in range(i, end):
                        u = a[j]
                        v = a[j + half] * w

                        a[j] = u + v
                        a[j + half] = u - v
                        w *= wlen

                length <<= 1

            if invert:
                inv_n = 1.0 / nfft
                for i in range(nfft):
                    a[i] *= inv_n

        f = [min(d, 26 - d) for d in range(26)]

        coeff = []
        for q in range(14):
            total = 0j
            for d in range(26):
                angle = -2.0 * math.pi * q * d / 26.0
                total += f[d] * complex(math.cos(angle),
                                        math.sin(angle))
            coeff.append(total / 26.0)

        size = 1
        while size < 2 * n - 1:
            size <<= 1

        contribution = [0.0] * n

        contribution = [coeff[0].real * n] * n

        for q in range(1, 14):
            arr = [0j] * size

            factor = 2.0 * math.pi * q / 26.0
            for i, x in enumerate(a):
                angle = factor * x
                arr[i] = complex(math.cos(angle), math.sin(angle))

            fft(arr)

            prod = [0j] * size
            for j in range(size):
                prod[j] = arr[j] * arr[(-j) & (size - 1)].conjugate()

            fft(prod, invert=True)

            cq = coeff[q]

            multiplier = 2.0 if q != 13 else 1.0

            for k in range(n):
                r = (2 * k - 1) % n

                value = prod[r].real

               
                if r + n < 2 * n - 1:
                    value += prod[r + n].real

                contribution[k] += multiplier * (cq * value).real

        
        ans = float("inf")

        for k in range(n):
            cost = k + contribution[k] / 2.0
            ans = min(ans, round(cost))

        return int(ans)