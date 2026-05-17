class Solution:
    def sumScores(self, s):
        def calculate_z_values(seq):
            n = len(seq)
            z_values = [0] * n
            window_start, window_end = 0, 0

            for index in range(1, n):
                if index <= window_end:
                    z_values[index] = min(window_end - index + 1, z_values[index - window_start])
                while index + z_values[index] < n and seq[z_values[index]] == seq[index + z_values[index]]:
                    z_values[index] += 1
                if index + z_values[index] - 1 > window_end:
                    window_start, window_end = index, index + z_values[index] - 1

            return z_values

        return len(s) + sum(calculate_z_values(s))