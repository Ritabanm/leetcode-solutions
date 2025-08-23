P = 701  # A base for polynomial hashing
MOD = 10**9 + 7  # Large prime for modulo operations

def precompute_hashes_and_inverses(s: str, p: int = P, mod: int = MOD):
    n = len(s)
    prefix_hashes = [0] * (n + 1)
    p_powers = [1] * (n + 1)
    p_inverses = [1] * (n + 1)

    # Precompute powers of p and their modular inverses
    for i in range(1, n + 1):
        p_powers[i] = (p_powers[i - 1] * p) % mod

    # Fermat's Little Theorem for calculating p^(-1) mod MOD
    p_inverses[n] = pow(p_powers[n], mod - 2, mod)
    for i in range(n - 1, 0, -1):
        p_inverses[i] = (p_inverses[i + 1] * p) % mod

    # Precompute prefix hashes
    for i in range(n):
        prefix_hashes[i + 1] = (prefix_hashes[i] + (ord(s[i]) - ord('a') + 1) * p_powers[i]) % mod

    return prefix_hashes, p_powers, p_inverses

def get_substring_hash(l: int, r: int, prefix_hashes, p_inverses, mod: int = MOD):
    # Hash of substring s[l:r+1] using the prefix hashes
    hash_value = (prefix_hashes[r + 1] - prefix_hashes[l] + mod) % mod
    # Normalize by multiplying by the modular inverse of p^l
    return (hash_value * p_inverses[l]) % mod

class Solution:

    def check_diff_count(self, l, r, i, j):
        # Track the number of differences between two substrings using a stack
        diff_count = 0
        stack = [(l, r, i, j)]

        while stack:
            l, r, i, j = stack.pop()

            if l > r:
                continue

            # Get the hash of the current substring in s and the pattern
            curr_hash = get_substring_hash(l, r, self.shashes, self.s_inverses)
            shash = get_substring_hash(i, j, self.phashes, self.p_inverses)

            # If the entire substring matches, continue
            if curr_hash == shash:
                continue

            # If comparing single characters, increment the difference count if they don't match
            if l == r and i == j:
                if self.s[l] != self.pattern[j]:
                    diff_count += 1
                    if diff_count > 1:
                        return diff_count
                continue

            # Split the current range and push both halves onto the stack
            mid = (l + r) // 2
            midi = (i + j) // 2

            stack.append((l, mid, i, midi))
            stack.append((mid + 1, r, midi + 1, j))

            # Early exit if more than one difference is found
            if diff_count > 1:
                return diff_count

        return diff_count

    def minStartingIndex(self, s: str, pattern: str) -> int:
        self.s = s
        self.pattern = pattern
        self.shashes, self.spowers, self.s_inverses = precompute_hashes_and_inverses(s)
        self.phashes, self.ppowers, self.p_inverses = precompute_hashes_and_inverses(pattern)

        n, m = len(s), len(pattern)

        # Check every substring of s that is of length m
        for i in range(n - m + 1):
            diff = self.check_diff_count(i, i + m - 1, 0, m - 1)
            if diff <= 1:
                return i

        return -1