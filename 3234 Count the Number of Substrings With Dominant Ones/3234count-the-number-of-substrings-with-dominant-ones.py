class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n, count = len(s), 0
        zero_indices = [-1]

        for i, char in enumerate(s):
            if char == '0':
                zero_indices.append(i)

            for l in range(len(zero_indices)):
                target_length = l * l + l
                if target_length > i + 1:
                    break

                left_index = zero_indices[-1 - l] if l < len(zero_indices) else -1
                right_index = zero_indices[-l] if l > 0 else i

                min_length = i - right_index + 1
                max_length = i - left_index

                if min_length >= target_length:
                    count += max_length - min_length + 1
                elif min_length <= target_length <= max_length:
                    count += max_length - target_length + 1

        return count